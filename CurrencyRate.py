# -*- coding: utf-8 -*-


class CurrencyRate:
    
    def __init__(self,currencyname,code,exchangerate):
        
        self.currencyname=currencyname
        self.code=code
        self.exchangerate=float(exchangerate)
        
    def getCurrencyRate(self):
        return self.exchangerate
        

        
        
    

