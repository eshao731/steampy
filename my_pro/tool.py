from pymongo import MongoClient


def db_table(_name):
    dbuser = 'root'
    dbpass = '1314520'
    dbip = '47.91.214.154:27017'
    dbname = 'admin'
    client = MongoClient('mongodb://{}:{}@{}/{}'.format(dbuser, dbpass, dbip, dbname))
    db = client['steam']
    return db[_name]


def get_short_id(steam_id):
    return int(steam_id) - 76561197960265728


if __name__ == '__main__':
    print(get_short_id('76561198840312182'))
