class Price:

    def __init__(self, symbol) :
        self.symbol = (symbol + 'USDT').upper()
        self.price = {'symbol': self.symbol} 

    def Binance(self):
        from binance.client import Client
        # import binance.exceptions
        api_key = ''
        api_secret = ''
        client = Client(api_key, api_secret)                
        # try:
        price = client.get_symbol_ticker(symbol=self.symbol)
        self.price['Binance'] =  price['price']
        # except binance.exceptions.BinanceAPIException:
                                                    
    def getPrice(self):
        self.Binance()
        return self.price




