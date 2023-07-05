from datetime import datetime

LOG = open('log.txt', 'w')

def timestamp():

    time = datetime.now()
    return f'[{time.year}/{time.month}/{time.day}] [{time.hour}:{time.minute}]'

def log(message):
    '''
    output nice version of message to log
    '''
    msg = f'{timestamp()} {repr(message)} \n'

    return LOG.write(msg) 