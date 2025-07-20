class TradeSetup:
    """
    a class representing one single trade setup
    """
    @property
    def entry_price(self):
        return self.__entry_price
    @entry_price.setter
    def entry_prive(self, entry_price):
        self.__entry_price = entry_price

    @property
    def exit_price(self):
        return self.__entry_price
    @entry_price.setter
    def exit_prive(self, exit_price):
        self.__exit_price = exit_price

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount