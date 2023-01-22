import requests

api_url='https://api.bitso.com/v3/ticker/?book=btc_mxn'
data=requests.get(api_url).json()
precio=float(data['payload']['last'])
print('El precio de BTC-MXN ES : ',precio)
#transformar pesos a btc
def price_mxn_btc(amountMxn):
    cantidad= amountMxn/ precio
    print('precio de btc en mxn',precio)
    print('cantidad a convertir : ',amountMxn)
    print(f'cantidad de btc : {cantidad:.8f} BTC')

amountMxn=float(input('ingrese la cantidad a convertir de mxn a btc : '))
price_mxn_btc(amountMxn)

