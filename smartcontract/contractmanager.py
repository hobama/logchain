import json
import threading
import pickle
import time
from queue import Queue

CONTRACT_ADDR = "_ContractStorage."
SOURCE_ADDR = "SmartContractManager.Sources."

contract_transaction_queue = Queue()


class ContractManager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            transaction = contract_transaction_queue.get()

            datas = json.dump(transaction, default=lambda o: o.__dict__, sort_keys=True)

            time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime())

            if datas['type'] == 'CT':
                # CT TYPE 시퀀스
                self.deploy_contract(time_stamp, 'example.py', 10)

            elif datas['type'] == 'RT':
                # RT TYPE 시퀀스
                result = self.execute_contract(time_stamp, 'C21341251325312', 'add', 3)
                print(result)

    def deploy_contract(self, time_stamp, sourcepath, args):
        contract = getattr(SOURCE_ADDR+sourcepath, 'Contract')(*args)
        contract_addr = "C"+time_stamp

        f_contract = open(CONTRACT_ADDR + contract_addr, 'wb')
        pickle.dump(contract, f_contract)
        f_contract.close()

        f_contract = open(CONTRACT_ADDR + contract_addr, 'rb')
        state = f_contract.read()
        f_contract.close()

        print('Contract(' + contract_addr + ') deployed')
        return {'contractAddr': contract_addr, 'state': state}

    def execute_contract(self, contract_addr, function, args):
        contractAddress = CONTRACT_ADDR + contract_addr
        print(contractAddress)

        # read contract file
        fContract = open(contractAddress, 'r')
        contract = pickle.load(fContract)
        print('Contract loaded')
        method = getattr(contract, function)

        # run method
        result = method(*args)
        fContract.close()

        # save state
        fContract = open(contractAddress, 'w')
        pickle.dump(contract, fContract)
        fContract.close()

        # load state
        fContract = open(contractAddress, 'r')
        state = fContract.read()
        fContract.close()

        print('Contract run : result : ' + str(result))
        return {'result': result, 'state': state}
