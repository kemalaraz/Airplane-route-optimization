# -*- coding: utf-8 -*-


from CurrencyRate import CurrencyRate
import csv

class CurrencyRateList:

    currencyratedict={} #Class object attribute

    def __init__(self,filename):

        self.currencyratedictionary=self.loadData(filename)

    def loadData(self,filename):

        with open(filename,encoding="utf8") as filename:

            reader=csv.reader(filename)

            try:
                for row in reader:
                    self.currencyratedict[row[1]]= CurrencyRate(row[0],row[1],row[2])

            except FileNotFoundError:
                print("File not found")

    def getCurrencyRate(self,code):

        """
        gets the currency code

        **Parameters**\n
        ----------\n
        code: gets the rate of the currency
        """
        currencyrate=self.currencyratedict[code]
        return currencyrate.getCurrencyRate()
