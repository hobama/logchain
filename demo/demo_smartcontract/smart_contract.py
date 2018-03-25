import time
import json

"""
    Construct Demo smartContract class
"""

class smartContract(object):

    def __init__(self, title, body):  # rule tx에서는 recv addr이 불요하므로 제거
        """
        :param title
        :param body
        """
        self.title = title
        self.body = body
        self.type = 'CT'

'''
# =====MODULE TEST=====
if __name__ == '__main__':
    title = "example.py"
    body = " class Contract(object): def __init__(self,pointName): self.pointName = pointName self.users = {} def add_point(self,user,point): point = int(point) users = self.users if user in users: users[user] += point else: users[user] = point return users[user]"
    smartContract = smartContract(title,body)
    smartContract = json.dumps(smartContract, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    temps = json.loads(smartContract)
    print (temps)
'''