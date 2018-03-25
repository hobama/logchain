import requests
from demo.demo_savetx import transaction_generator

def post_transaction(url,tx):
    url = url
    tx = tx
    response=requests.post(url,tx)
    return response


'''
if __name__ == "__main__":
    url = "http://163.239.200.180:5000/tx/save"
    tx = transaction_generator.transaction_generator()
    post_transaction(url,tx)
'''