import logging
from logging.handlers import SocketHandler

log = logging.getLogger('Root logger')
log.setLevel(1)  # to send all messages to cutelog
socket_handler = SocketHandler('127.0.0.1', 19996)  # default listening address
log.addHandler(socket_handler)
log.info('Hello world!')
log.info('Hello world2!')