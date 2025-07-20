class TradingPair:
    """
    represents a single trading pair
    """
    @property
    def trading_pair(self):
        return self.__trading_pair
    
    @trading_pair.setter
    def trading_pair(self, trading_pair):
        if not trading_pair:
            raise ValueError("TradingPair darf nicht leer sein")
        self.__trading_pair = trading_pair

    def __init__(self):
        self.__trading_pair = "btc/usdt"