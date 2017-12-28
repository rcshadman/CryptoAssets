import APICalls as api_calls
import json

# Toggle b/w displaying the 'high' or 'last' market values.
TYPE = 'last'



balance = api_calls.getBalance(api_calls.qkey, api_calls.qsecret, api_calls.clientID)
BTC_Amount = balance['btc_available']
BTG_Amount = balance['btg_available']
ETH_Amount = balance['eth_available']
BCH_Amount = balance['bch_available']


btc_data = api_calls.getBTCMarketData()
btg_data = api_calls.getBTGMarketData()
eth_data = api_calls.getETHMarketData()
bch_data = api_calls.getBCHMarketData()

btg_data = btg_data[TYPE]
btc_data = btc_data[TYPE]
eth_data = eth_data[TYPE]
bch_data = bch_data[TYPE]

BTG_CAD_VALUE = float(BTG_Amount)*float(btg_data)
BTC_CAD_VALUE = float(BTC_Amount)*float(btc_data)
ETH_CAD_VALUE = float(ETH_Amount)*float(eth_data)
BCH_CAD_VALUE = float(BCH_Amount)*float(bch_data)
TOTAL_CAD_VALUE = BTG_CAD_VALUE + BTC_CAD_VALUE + ETH_CAD_VALUE + BCH_CAD_VALUE
print 'BTG: ' + str(BTG_CAD_VALUE) + '($' + btg_data + '/BTG)'
print 'BTC: ' + str(BTC_CAD_VALUE) + '($' + btc_data + '/BTC)'
print 'ETH: ' + str(ETH_CAD_VALUE) + '($' + eth_data + '/ETH)'
print 'BCH: ' + str(BCH_CAD_VALUE) + '($' + bch_data + '/BCH)'
print 'Total: ' + str(TOTAL_CAD_VALUE)
