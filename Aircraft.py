# -*- coding: utf-8 -*-
class Aircraft:

    def __init__(self,code,types,units,manu,ranges):

        self.code=code
        self.types=types
        self.units=units
        self.manu=manu
        self.badranges=float(ranges)
        self.ranges=self.metric()

    def metric(self):

        """
        If the range metrics of the aircraft is in different form (imperial)
        convert it to metric

        **Returns**\n
        -------\n
        ranges: Atlered ranges of aircrafts
        """

        if self.units.lower()=='imperial':
            return self.badranges*1.609344
        else:
            return self.badranges
        

    def getAircraftRange(self):
        return self.ranges
