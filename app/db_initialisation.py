import sqlite3
from sqlite3 import OperationalError

log = open('log.txt', 'w')

CON = sqlite3.connect('inventory.db')

CUR = CON.cursor()

def create_table(name, *args):
    '''
    create a table with the name <name> and fields <*args>
    '''
    try:
        CUR.execute(f'CREATE TABLE {name}({", ".join(args)})')
        return f'TABLE {name} CREATED'
    except OperationalError as e:
        return f'ERROR ~ {e}'

# create one table for item quantities, one tabel for id lookup
log.write(create_table('inventory', 'id', 'quantity') + '\n')
log.write(create_table('id_lookup', 'id', 'name') + '\n')

with open('test-data.txt', 'r') as data:
    records = [tuple(i.split(' ')) for i in data.read().split('\n')]

    log.write(repr(records))

    KEY_inventory = (0, 2)
    KEY_id_lookup = (0, 1) 
    
    CUR.executemany('INSERT INTO inventory VALUES(?, ?)', [tuple(record[key] for key in KEY_inventory) for record in records])

res = CUR.execute('SELECT * FROM inventory')
print(res.fetchall())