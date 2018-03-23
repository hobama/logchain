import json
from smartcontract import contractmanager


def verify(block):
    for transaction in block.tx_list:
        data = json.dump(transaction, default=lambda o: o.__dict__, sort_keys=True)
        if data['type'] == 'CT':
            contractmanager.contract_transaction_queue.put(data)
        elif data['type'] == 'RT':
            contractmanager.contract_transaction_queue.put(data)
