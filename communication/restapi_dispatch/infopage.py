

# http://host:5000/info/tx/
SavedTxList = [
    {
        "tx_id": "The transaction ID",
        "tx_from_ip": "The IP of transaction sender",
        "tx_body": "Saved transaction data"
    }
]

def addSavedTx(transaction):
    saved_tx = {
        'tx_id': transaction.tx_id,
        'tx_from_ip': transaction.sender_ip,
        'tx_body': transaction.extra_data
    }
    SavedTxList.append(saved_tx)




# http://host:5000/info/contract/deployed/
DeployedSmartContractList = [
    {
        "smart_contract_tx_id": "The deployed smart contract transaction ID",
        "smart_contract_tx_from_ip": "The IP of transaction sender",
        "smart_contract_tx_body": "Deployed smart contract transaction data"
    }
]

def addDeployedContract(deployed_contract):
    deployed_cont = {
        'tx_id': deployed_contract.tx_id,
        'tx_from_ip': deployed_contract.sender_ip,
        'tx_body': deployed_contract.extra_data
    }
    DeployedSmartContractList.append(deployed_cont)



# http://host:5000/info/contract/executed/
ExecutedSmartContractList = [
    {
        "smart_contract_tx_id": "The executed smart contract transaction ID",
        "smart_contract_tx_from_ip": "The IP of transaction sender",
        "smart_contract_tx_body": "Executed smart contract transaction data"
    }
]

def addExecutedContract(executed_contract):
    deployed_cont = {
        'tx_id': executed_contract.tx_id,
        'tx_from_ip': executed_contract.sender_ip,
        'tx_body': executed_contract.extra_data
    }
    ExecutedSmartContractList.append(deployed_cont)


