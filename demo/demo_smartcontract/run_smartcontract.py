import time
import json

"""
    Construct Demo run smartContract class
"""

class runSmartContract(object):

    def __init__(self, address, parameter):  # rule tx에서는 recv addr이 불요하므로 제거
        """
        :param title
        :param body
        """
        self.parameter = parameter
        self.address = address
        self.type = 'RT'
