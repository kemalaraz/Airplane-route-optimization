# -*- coding: utf-8 -*-
from Airport import Airport
from math import sin,cos,acos,pi
import csv

class AirportAtlas:


    airportdict={} #Class object attribute
    def __init__(self,filename):

        self.airportdictionary=self.loadData(filename)

    def loadData(self,filename):

        """
        gets the filename and loads all the information
        about the Airports

        **Parameters**\n
        ----------\n
        filename: Airport data filename
        """

        with open(filename,encoding="utf8") as file:

            reader=csv.reader(file)

            try:
                for row in reader:
                    self.airportdict[row[4]]= Airport(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])


            except FileNotFoundError:
                print("File not found")

    def getAirportCountry(self,code):

        """
        gets the IATA code takes it to the function
        inside airport class and returns the airport's country

        **Parameters**\n
        ----------\n
        code: IATA code
        **Returns**\n
        -------\n
        country: country of the airport
        """

        airport=self.airportdict[code]
        return airport.getAirportCountry()

    def greatCircleDist(self,lat1,long1,lat2,long2):

        """
        gets the latitude and longitude of two airports and
        calcluates the circle distance between those Airports
        circle distance: The distance which takes earth's radius
        into account.

        **Parameters**\n
        ----------\n
        lat1: First airports latitude
        lat2: Second airports latitude
        long1: First airports longitude
        long2: Second airports longitude
        **Returns**\n
        -------\n
        distance: circle distance between airports
        """

        earthrad=6371
        return float(earthrad * acos((sin((90 - lat1) * 2 * pi / 360) * sin((90 - lat2) * 2 * pi / 360) * cos((long1 * 2 * pi / 360) - (long2 * 2 * pi / 360))) + cos((90 - lat1) * 2 * pi / 360) * cos((90 - lat2) * 2 * pi / 360)))


    def distanceBetweenAirports(self,code1,code2):

        """
        gets the IATA code of two airports which the distance wants to calculated
        takes the latitude and longitude of those airports invokes the greatCircleDist()
        function for finding the circle distance between those airports and returns the
        distance

        **Parameters**\n
        ----------\n
        code1: First airports IATA code
        code2: Second airports IATA code
        **Returns**\n
        -------\n
        distance: circle distance between airports
        """

        lat1,long1=self.airportdict[code1].getCoordinates()
        lat2,long2=self.airportdict[code2].getCoordinates()

        return self.greatCircleDist(lat1,long1,lat2,long2)
