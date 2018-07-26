import string
import random
import hmac


HashChain = []
ClientID = "clientA"
ChainLength: int = 1000
PrivateX = ""


ClientIDInServer = ""
PrivateXInServer = ""
ChainLengthInServer: int = 0
HashchainRoot = ""



# 1. 클라이언트는 비밀 키(x)를 임의로 생성
def GeneratingClientPrivateSeed() -> string:
    possibleChars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    privateSeed = ''.join(random.choice(possibleChars) for x in range(10))  # seed length는 최적화 정의 필요하고, 일단 10으로 정의
    return privateSeed



# 2. x와 n을 자신의 식별자와 함께 서버에게 전달 (서버 공개키 이용하여, 암호/복호화를 하거나, 다른 방식으로 공유하여 로컬에 저장 등)
def SendPrivateSeedToServer(clientID, privateSeed, chainLength) :
    global ClientIDInServer
    global PrivateXInServer
    global ChainLengthInServer

    ClientIDInServer = clientID
    PrivateXInServer = privateSeed
    ChainLengthInServer = chainLength




# 3. 클라이언트는 x를 사용하여 hash chain 방식으로 n개의 OTP를 생성하여 저장
def GeneratingClientHashChain(seed, n):
    prevHash = seed
    for i in range(1, n+1, 1):
        newHash = hmac.new(prevHash.encode(), digestmod="sha256").hexdigest()
        HashChain.append(newHash)
        prevHash = newHash
        # print(i, newHash)


# 4. 서버는 클라이언트로부터 클라이언트의 비밀 키를 첫 값으로 사용하여, hash chain 방식으로 이전 결과 값에 대한 hash를 구하는 연산을 n번 수행
#    최종적으로 클라이언트 식별자와 n, h_n+1(x)를 저장
def GeneratingRootHashValue(seed, n) :
    global HashchainRoot
    prevHash = seed
    for i in range(1, n+1, 1):
        newHash = hmac.new(prevHash.encode(), digestmod="sha256").hexdigest()
        prevHash = newHash

    HashchainRoot = prevHash




# 6. 서버는 클라이언트로부터 받은 값에 hash를 적용하여, 그 결과가 서버에 저장된 root hash 값과 동일한지 검사
def AuthTransferByServer(msg, clientKey, counter) -> bool :
    global HashchainRoot
    newHash = hmac.new(clientKey.encode(), digestmod="sha256").hexdigest()


    if (newHash == HashchainRoot) :
        # 7. 일치하면 인증 성공
        #    인증에 성공하면 서버에 저장된 n-counter+1 값을 n-counter로 1 감소시키고 h_n-counter+1(x)를 h_n-counter(x)로 수정
        GeneratingRootHashValue(PrivateXInServer, ChainLengthInServer - counter)
        print("Server: auth success / rcvd msg:", msg)
        return True
    else :
        print("Server: auth failure / rcvd msg:", msg)
        # 8. 인증에 실패하면 서버에 저장된 값은 그대로 유지
        return False


def SendToServer(msg, counter) :
    global PrivateX
    prevHash = PrivateX
    # 5. 클라이언트에서 정한 비밀 키에 hash함수를 n-counter번 적용하여 서버로 전송
    for i in range(1, ChainLength - counter + 1, 1):
        newHash = hmac.new(prevHash.encode(), digestmod="sha256").hexdigest()
        prevHash = newHash

    if AuthTransferByServer(msg, prevHash, counter):
        print("Client: transfer success")
    else:
        print("Client: transfer failure")


if __name__ == '__main__':

    PrivateX = GeneratingClientPrivateSeed()
    SendPrivateSeedToServer(ClientID, PrivateX, ChainLength)
    GeneratingClientHashChain(PrivateX, ChainLength)
    GeneratingRootHashValue(PrivateX, ChainLength)

    # testing

    # 1번째로 서버에 메시지 전송 인증을 요구 / expected = success
    msg = "hello (counter: 1)"
    counter = 1
    SendToServer(msg, counter)

    # 2번째로 서버에 메시지 전송 인증을 요구 / expected = success
    msg = "hi (counter: 2)"
    counter = 2
    SendToServer(msg, counter)

    # 4번째로 서버에 메시지 전송 인증을 요구 / expected = failure
    msg = "good morning (counter: 4)"
    counter = 4
    SendToServer(msg, counter)


