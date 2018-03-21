import json
import threading
from queue import Queue

contract_transaction_queue = Queue()


class ContractManager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if contract_transaction_queue.qsize() > 0:
                transaction = contract_transaction_queue.get()

                datas = json.dump()

                if datas['type'] == 'CT':
                    # CT TYPE 시퀀스
                    pass

                elif datas['type'] == 'RT':
                    # RT TYPE 시퀀스
                    pass

    def deploy_contract(self, filepath):
        pass

    def execute_contract(self, c_address):
        pass
