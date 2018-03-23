import pickle
import time

CONTRACT_ADDR = "_ContractStorage."
SOURCE_ADDR = "smartcontract.Sources."


class ContractManager():
    def __init__(self):
        pass

    def deploy_contract(self, time_stamp, sourcefile, args):
        contract = getattr(sourcefile, 'Contract')(*args)
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
        fContract = open(contractAddress, 'rb')
        contract = pickle.load(fContract)
        print('Contract loaded')
        method = getattr(contract, function)

        # run method
        result = method(*args)
        fContract.close()

        # save state
        fContract = open(contractAddress, 'wb')
        pickle.dump(contract, fContract)
        fContract.close()

        # load state
        fContract = open(contractAddress, 'rb')
        state = fContract.read()
        fContract.close()

        print('Contract run : result : ' + str(result))
        return {'result': result, 'state': state}
