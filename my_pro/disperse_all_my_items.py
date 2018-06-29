import re
import datetime

from steampy.bot_trade import BotTrade

from tool import db_table, get_short_id

if __name__ == '__main__':
    table = db_table('bot')
    table_offer = db_table('offer')
    send_col = table.find_one({'username': 'eshao731'})
    send_client = BotTrade(send_col)

    bot_list = {}
    for i in table.find({'status': 'running'}):
        trade_url = 'https://steamcommunity.com/tradeoffer/new/?partner={}&token={}'.format(
            get_short_id(i['SteamID']),
            i['trade_token']
        )
        is_ban = send_client.steam_client.check_bot_is_ban(trade_url)
        if not is_ban:
            bot_list['trade_url'] = str(i['SteamID'])

    offer_list = send_client.send_all_items_to_many(bot_list.keys())
    for i in offer_list:
        trade_url, offer_id = i
        result = dict(
            send_id=str(send_col['SteamID']),
            target_id=bot_list['trade_url'],
            offer_id=offer_id,
            datetime=datetime.datetime.now(),
            finish=False
        )
        x = table_offer.insert(result)
        print(x)
