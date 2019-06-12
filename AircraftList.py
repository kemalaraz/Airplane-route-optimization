# -*- coding: utf-8 -*-

from Aircraft import Aircraft
import csv


class AircraftList:

    aircraftdict={} #Class object attribute

    def __init__(self,filename):

        self.aircrafdict=self.loadData(filename)

    def loadData(self,filename):

        """
        gets the filename and loads all the information
        about the Aircraft

        **Parameters**\n
        ----------\n
        filename: Aircraft data filename
        """


        with open(filename,encoding="utf8") as file:

            reader=csv.reader(file)

            try:
                for row in reader:
                    self.aircraftdict[row[0]]= Aircraft(row[0],row[1],row[2],row[3],row[4])



            except FileNotFoundError:
                print("File not found")

    def getAircraftRange(self,code):
        aircraft=self.aircraftdict[code]
        return aircraft.getAircraftRange()
