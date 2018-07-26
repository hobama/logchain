import pyotp
import time

# HMAC based OTP
def testHOTPBasedComm():
    hotp = pyotp.HOTP('base32secret3232')
    print(hotp.at(0))  # => '260182'
    print(hotp.at(1))  # => '055283'
    print(hotp.at(1401))  # => '316439'

    # OTP verified with a counter
    print(hotp.verify('316439', 1401))  # => True
    print(hotp.verify('316439', 1402))  # => False


# Time based OTP
def testTOTPBasedComm():
    totp = pyotp.TOTP('base32secret3232')
    otp = totp.now()
    print(otp)  # => '492039'

    # OTP verified for current time
    print(totp.verify(otp))  # => True
    time.sleep(10)
    print(totp.verify('492039'))  # => False



if __name__ == '__main__':
    print("HOTP testing.......")
    testHOTPBasedComm()

    print("TOTP testing.......")
    testTOTPBasedComm()



