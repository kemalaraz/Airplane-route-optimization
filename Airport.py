# -*- coding: utf-8 -*-


class Airport:

    def __init__(self,airport_id,name,city,country,code,icacode,lat,long,alt,toffset,DST,Tz):

        self.airport_id=int(airport_id)
        self.name=name
        self.city=city
        self.country=country
        self.code=code
        self.icacode=icacode
        self.lat=float(lat)
        self.long=float(long)
        self.alt=float(alt)
        self.toffset=float(toffset)
        self.DST=DST
        self.Tz=Tz

    def getCoordinates(self):

        """
        Returns the latitude
        and longitude related with IATA code

        **Returns**\n
        -------\n
        self.lat: latitude
        self.long: longitude
        """

        return self.lat, self.long

    def getAirportCountry(self):

        """
        gets the IATA code and returns the country
        of that airport.

        **Returns**\n
        -------\n
        self.country: country of the airport
        """

        return self.country
