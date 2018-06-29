from steampy.bot_trade import BotTrade

from tool import db_table

if __name__ == '__main__':
    table = db_table('bot')
    table_offer = db_table('offer')
    receive_col = table.find_one({'username': 'star777star'})
    my_client = None

    for i in table_offer.find({'target_id': str(receive_col['SteamID']), 'finish': False}):
        if not my_client:
            my_client = BotTrade(receive_col)
        finish = my_client.accept(i['offer_id'])
        x = table_offer.update({'_id': i['_id']}, {'$set': {'finish': finish}})
        print(x)
