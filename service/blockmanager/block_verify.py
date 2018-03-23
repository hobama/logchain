import json
from smartcontract import contractmanager


def verify(block):
    ctmgr = contractmanager.ContractManager()
    for transaction in block.tx_list:
        data = json.dump(transaction, default=lambda o: o.__dict__, sort_keys=True)
        if data['type'] == 'CT':
            ctmgr.deploy_contract(data['extra_data']['source'], data['extra_data']['args'])

        elif data['type'] == 'RT':
            ctmgr.execute_contract(data['extra_data']['contract_addr'], data['extra_data']['function'], data['extra_data']['args'])