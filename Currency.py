# -*- coding: utf-8 -*-


class Currency:

    def __init__(self,countryname,code,currencyname):

        self.countryname=countryname
        self.code=code
        self.currencyname=currencyname

    def getCurrencyCode(self):

        """
        gets the currency code

        **Parameters**\n
        ----------\n
        code: gets the abbreviation of the currency
        """
        
        return self.code
