import datetime

from steampy.bot_trade import BotTrade

from tool import db_table, get_short_id

if __name__ == '__main__':
    table = db_table('bot')
    table_offer = db_table('offer')
    receive_col = table.find_one({'username': 'eshao731'})
    send_col = table.find_one({'username': 'star777star'})

    trade_offer_url = 'https://steamcommunity.com/tradeoffer/new/?partner={}&token={}'.format(
        get_short_id(receive_col['SteamID']),
        receive_col['trade_token']
    )

    t = BotTrade(send_col)
    offer_list = t.send_all_items(trade_offer_url)
    for i in offer_list:
        result = dict(
            send_id=str(send_col['SteamID']),
            target_id=str(receive_col['SteamID']),
            offer_id=i,
            datetime=datetime.datetime.now(),
            finish=False
        )
        x = table_offer.insert(result)
        print(x)
