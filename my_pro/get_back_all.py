import time

from steampy.bot_trade import BotTrade

from tool import db_table, get_short_id

if __name__ == '__main__':
    table = db_table('bot')
    table_offer = db_table('offer')
    target_col = table.find_one({'username': 'star777star'})
    short_id = get_short_id(target_col['SteamID'])
    trade_offer_url = 'https://steamcommunity.com/tradeoffer/new/?partner={}&token={}'.format(short_id,
                                                                                              target_col['trade_token'])

    for i in table.find({'status': 'running'}):
        t = BotTrade(i)
        resp = t.send_all_itmes(trade_offer_url)
        offer_id = resp['tradeofferid']
        x = table_offer.insert(dict(steam_id=str(target_col['SteamID']), offer_id=offer_id))
        time.sleep(30)

    # 目标账户接收报价
    target = BotTrade(target_col)
    for i in table_offer.find({'steam_id': str(target_col['SteamID'])}):
        target.accept(i['offer_id'])
        time.sleep(10)
        x = table_offer.remove({'_id': i['_id']})
        print(x)

    # user = 'star777star'
    # pwd = 'star7777777STAR'
    # api_key = '9945BB4F22B10452D794F6A5468AB3AE'
    # steam_guard = {
    #     "steamid": "76561198805934271",
    #     "shared_secret": "s+U7B4zmv6xqvluliqvyFH2Ewqk=",
    #     "identity_secret": "I3gkSRe/VbV3HuCmYoBovhCxQdY=",
    # }
    # trade_offer_url = 'https://steamcommunity.com/tradeoffer/new/?partner=151540833&token=7uBboQY2'
    # t = TradeAll(user, pwd, api_key, steam_guard, trade_offer_url)

    # user_list = ['pfuwfr0glv', 'vzdk5rw30c', 'dhygr4fqje', 'xisky111']
    # pwd_list = ['hcPEUb23Ma', 'OB1VHCUxDJ', 'kVbH19laP6', 'english731']
    # api_key_list = ['7375BB48BB687166FE267EE48F528277',
    #                 'D1556D1D1BD31D34EFDB0A2377719EBF',
    #                 'D0763FDD6673D0614DA24DD4AB14845F',
    #                 '9F4241FAE4D643BC885829F1E50A1B7B']
    # steam_guard_list = []
    # steam_guard_list.append({
    #     "steamid": "76561198840312182",
    #     "shared_secret": "Kb55CcI3thhfkOU9k7VT1YM7/ko=",
    #     "identity_secret": "6mm3kPxh6LRzI1ef/Pws10CRCe4=",
    # })
    # steam_guard_list.append({
    #     "steamid": "76561198840457970",
    #     "shared_secret": "LD5erjdgkTwbyyeINcmWhr6SGH0=",
    #     "identity_secret": "FzB/zUloZc14WjM/x7bjUZryxJc=",
    # })
    # steam_guard_list.append({
    #     "steamid": "76561198840413167",
    #     "shared_secret": "fTWQ4KQbMe+6+lMAsL7OEioryY0=",
    #     "identity_secret": "tUsHEL1Raicc5HofIjPRAuzCp8o=",
    # })
    # steam_guard_list.append({
    #     "steamid": "76561198263343462",
    #     "shared_secret": "VuduPi5c2DSrlftwHmsctWbiAGo=",
    #     "identity_secret": "iuGDPrEhUIiRXVhryQAyjdftiu4=",
    # })
    # for i in range(4):
    #     t = TradeAll(user_list[i], pwd_list[i], api_key_list[i], steam_guard_list[i], trade_offer_url)
    #     t.run()
    #     time.sleep(30)
