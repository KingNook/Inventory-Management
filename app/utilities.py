from datetime import datetime

def timestamp():

    time = datetime.now()
    return f'[{time.year}/{time.month}/{time.day}] [{time.hour}:{time.minute}:{int(time.second)}]'

curtime = datetime.now()

LOG = open('./logs/LOG_{0:02d}-{1:02d}-{2}_{3:02d}-{4:02d}-{5:02d}.txt'.format(curtime.day, curtime.month, curtime.year, curtime.hour, curtime.minute, curtime.second), 'w')

def log(message):
    '''
    output nice version of message to log
    '''
    msg = f'{timestamp()} {repr(message)} \n'

    return LOG.write(msg) 

log(f'Log created {timestamp()}')