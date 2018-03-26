import requests
from demo.demo_savetx import transaction_generator
import json
def post_transaction(url,tx):
    url = url
    tx = tx
    print(tx)
    response=requests.post(url,data=json.dumps(tx))
    return response



if __name__ == "__main__":
    url = "http://163.239.200.180:5000/tx/save"
    #tx = transaction_generator.transaction_generator()
    tx = "test"
    response=post_transaction(url,tx)
    print(response)