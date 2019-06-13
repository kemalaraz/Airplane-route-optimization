# -*- coding: utf-8 -*-


from Currency import Currency
import csv

class CurrencyList:

    currencydict={} #Class object attribute

    def __init__(self,filename):

        self.currencydictionary=self.loadData(filename)

    def loadData(self,filename):

        with open(filename,encoding="utf8") as filename:

            reader=csv.reader(filename)

            try:
                for row in reader:
                    self.currencydict[row[0]]= Currency(row[0],row[14],row[17])

            except FileNotFoundError:
                print("File not found")

    def getCurrencyCode(self,code):

        """
        gets the code of the currency invokes the getCurrencyCode() from
        the Currency class and returns the currency abbreviation.

        **Parameters**\n
        ----------\n
        filename: Airport data filename
        """
        currencycode=self.currencydict[code]
        return currencycode.getCurrencyCode()
