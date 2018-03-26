import json
from smartcontract import contractmanager
from communication.restapi_dispatch import infopage

def verify_tx_list(tx_list):
    contract_manager = contractmanager.ContractManager()
    for transaction in tx_list:
        data_jobj = json.loads(transaction)
        if data_jobj['type'] == 'CT':
            contract_manager.deploy_contract(
                data_jobj['timestamp'],
                data_jobj['extra_data']['contract_body'],
                data_jobj['extra_data']['contract_args']
            )
            infopage.addDeployedContract(transaction)
        elif data_jobj['type'] == 'RT':
            contract_manager.execute_contract(
                data_jobj['extra_data']['contract_addr'],
                data_jobj['extra_data']['contract_function'],
                data_jobj['extra_data']['contract_args']
            )
            infopage.addExecutedContract(transaction)
        elif data_jobj['type'] == 'T':
            infopage.addSavedTx(transaction)


        # data = json.dumps(transaction, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        # if data['type'] == 'CT':
        #     contract_manager.deploy_contract(data['extra_data']['contract_body'], data['extra_data']['contract_args'])
        #
        # elif data['type'] == 'RT':
        #     contract_manager.execute_contract(data['extra_data']['contract_addr'], data['extra_data']['contract_function'], data['extra_data']['contract_args'])


def verify(block):
    contract_manager = contractmanager.ContractManager()
    for transaction in block.tx_list:
        data = json.dumps(transaction, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        if data['type'] == 'CT':
            contract_manager.deploy_contract(data['extra_data']['contract_body'], data['extra_data']['contract_args'])

        elif data['type'] == 'RT':
            contract_manager.execute_contract(data['extra_data']['contract_addr'], data['extra_data']['contract_function'], data['extra_data']['contract_args'])