# -*- coding: utf-8 -*-

from Itinerary import Itinerary
from AirportAtlas import AirportAtlas
from AircraftList import AircraftList
from CurrencyList import CurrencyList
from CurrencyRateList import CurrencyRateList
from itertools import permutations
import sys
from tkinter import messagebox



class ItineraryList:


    def __init__(self,Data):

        self.__routelist=self.loadData(Data)

    def loadData(self,Data):

        numofairports=len(Data)-1 #minus one because last index is aircraftcode

        airportlist=[]

        for i in range(numofairports): #seperates airports from aircraft
            airportlist.append(Data[i])

        aircraftcode=Data[numofairports]

        cheapestroutelist,mincost,cheapestroutedist,shortestroutelist,shortestroutecost,shortestroutedist=ItineraryList.calculationForFiveRoutes(self,airportlist,aircraftcode)
        self.obj1=Itinerary(cheapestroutelist,mincost,cheapestroutedist,shortestroutelist,shortestroutecost,shortestroutedist,Data[5])

    def getCheapestRouteList(self):
        return self.obj1.getCheapestRouteList()

    def getMinCost(self):
        return self.obj1.getMinCost()

    def getCheapestRouteDist(self):
        return self.obj1.getCheapestRouteDist()

    def getShortestRouteList(self):
        return self.obj1.getShortestRouteList()

    def getShortestRouteCost(self):
        return self.obj1.getShortestRouteCost()

    def getShortestRouteDist(self):
        return self.obj1.getShortestRouteDist()

    def getAircraft(self):
        return self.obj1.getAircraft()



    def permutations(homeairport,airportlist):

        possairportlist=list(permutations(airportlist))
        routelist=[]
        for row in possairportlist:
            row=list(row)
            row.insert(0,homeairport)
            row.insert(len(row),homeairport)
            routelist.append(row)
        return routelist

    def calculationForFiveRoutes(self,airportlist,aircraftcode):

        """
        The main code of the project. Takes the list of the airports and aircraft
        given by the user, eliminates all the impossible routes and with trial and
        error finds the optimum route. Returns the cheapest route, minimum cost,
        distance of the optimum route and the impossible routes distance.

        cheapestroutelist,mincost,routedist,impossible_routes_distancefuel
        **Parameters**\n
        ----------\n
        airportlist: A list consists of 5 airports (IATA codes) taken as an input
        from the user.
        aircraftcode: The aircraft's code which will carry on the itinerary.

        **Returns**\n
        -------\n
        cheapestroutelist: The sequence of airports regarding to the optimum route.
        mincost: The cost of the itinerary.
        routedist: THe total distance of the itinerary.
        impossible_routes_distancefuel: The list of the impossible routes.

        """


        homeairport=airportlist.pop(0)

        routelist=ItineraryList.permutations(homeairport,airportlist)
        cheapestroutelist,mincost,routedist,bestroutelist,cost1,bestroute,impossible_routes_fullrefuel=ItineraryList.fullrefuel(airportlist,routelist,aircraftcode)
        cheapestroutelistopt,mincostopt,routedistopt,impossible_routes_distancefuel=ItineraryList.distancerefuel(airportlist,routelist,aircraftcode)
        if mincostopt<mincost:
            mincost=mincostopt
            cheapestroutelist=cheapestroutelistopt
            routedist=routedistopt

        if len(impossible_routes_fullrefuel)==24 and len(impossible_routes_distancefuel)==24: #if all possible routes=(4!)*2 are impossible print ...
            messagebox.showinfo("Impossible route", "This plane cannot complete the specified routes please change the plane or routes")

        elif len(impossible_routes_fullrefuel)==24:
            mincost=mincostopt
            cheapestroutelist=cheapestroutelistopt
            routedist=routedistopt


        else:

            return cheapestroutelist,mincost,routedist,bestroutelist,cost1,bestroute

    def fullrefuel(airportlist,routelist,aircraftcode): #finds shortest and cheapest routes by full refuel

        try:
            aircraft=AircraftList('aircraft.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error aircraft.csv file", "Unable to load 'aircraft.csv' file please make sure this file and aircraft.csv located on the same file and filename is 'aircraft.csv'")
            sys.exit(0)

        try:
            airport=AirportAtlas('airport.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error airport.csv file", "Unable to load 'airport.csv' file please make sure this file and airport.csv located on the same file and filename is 'airport.csv'")
            sys.exit(0)

        try:
            countrycurr=CurrencyList('countrycurrency.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error countrycurrency.csv file", "Unable to load 'countrycurrency.csv' file please make sure this file and countrycurrency.csv located on the same file and filename is 'countrycurrency.csv'")
            sys.exit(0)

        try:
            currencyrate=CurrencyRateList('currencyrates.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error currencyrates.csv file", "Unable to load 'currencyrates.csv' file please make sure this file and currencyrates.csv located on the same file and filename is 'currencyrates.csv'")
            sys.exit(0)
        # some initial assignments
        initialaircraftrange=aircraft.getAircraftRange(aircraftcode)
        aircraftrange=initialaircraftrange
        bestroute=10**10
        mincost=10**10
        tobefueled=0
        cost=0
        indx=0
        currrate=0
        impossible_routes_fullrefuel=[]
        control=0 #for controling the impossible routes

        for j in range(len(routelist)):

            totalcost=0
            totalroute=0
            control=0 #sets control back to zero
            for k in range(len(airportlist)+1):


                distance=airport.distanceBetweenAirports(routelist[j][k],routelist[j][k+1])
                totalroute+=distance

                if routelist[j][k]==routelist[j][k+1]: #plane can visit one airport twice but departure and arrival cant be same airport
                    control=1

                if distance>aircraftrange:

                    tobefueled=initialaircraftrange-aircraftrange
                    where=airport.getAirportCountry(routelist[j][k])
                    iseuro=countrycurr.getCurrencyCode(where)
                    currrate=currencyrate.getCurrencyRate(iseuro)
                    cost=tobefueled*currrate
                    aircraftrange+=tobefueled
                    totalcost+=cost


                if distance>aircraftrange: #still distance is bigger than range even when gas tank is full
                    control=1 #if control is 1 bestroute and cheapest is not calculated

                indx+=1

                aircraftrange=aircraftrange-distance

            totalroute1=totalroute
            aircraftrange=initialaircraftrange
#================COMPARING===============================
            if control == 0:

                if bestroute>totalroute:
                    bestroute=totalroute
                    bestroutelist=routelist[j]
                    cost1=totalcost

                if mincost>totalcost:
                    mincost=totalcost
                    cheapestroutelist=routelist[j]
                    routedist=totalroute1
#=========================================================

            else:
                impossible_routes_fullrefuel.append(routelist[j]) # for counting impossible routes
                bestroutelist=0
                totalroute=0
                cost1=0
        if len(impossible_routes_fullrefuel)==24:
            cheapestroutelist=0
            mincost=10**10
            routedist=0
            bestroutelist=0
            cost1=10**10
            bestroute=0
            return cheapestroutelist,mincost,routedist,bestroutelist,cost1,bestroute,impossible_routes_fullrefuel
        else:
            return cheapestroutelist,mincost,routedist,bestroutelist,cost1,bestroute,impossible_routes_fullrefuel

    def distancerefuel(airportlist,routelist,aircraftcode): #Doing a small optimization by checking whether fully refueling or refueling enough for only that leg's distance is cheaper

        try:
            aircraft=AircraftList('aircraft.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error aircraft.csv file", "Unable to load 'aircraft.csv' file please make sure this file and aircraft.csv located on the same file and filename is 'aircraft.csv'")
            sys.exit(0)

        try:
            airport=AirportAtlas('airport.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error airport.csv file", "Unable to load 'airport.csv' file please make sure this file and airport.csv located on the same file and filename is 'airport.csv'")
            sys.exit(0)

        try:
            countrycurr=CurrencyList('countrycurrency.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error countrycurrency.csv file", "Unable to load 'countrycurrency.csv' file please make sure this file and countrycurrency.csv located on the same file and filename is 'countrycurrency.csv'")
            sys.exit(0)

        try:
            currencyrate=CurrencyRateList('currencyrates.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error currencyrates.csv file", "Unable to load 'currencyrates.csv' file please make sure this file and currencyrates.csv located on the same file and filename is 'currencyrates.csv'")
            sys.exit(0)

        initialaircraftrange=aircraft.getAircraftRange(aircraftcode)
        aircraftrange=initialaircraftrange
        mincost=10**10
        totalcostopt=0
        indx=0
        currrate=0
        impossible_routes_distancefuel=[]
        control=0

        for j in range(len(routelist)):
            totalroute=0
            totalcostopt=0
            control=0
            for k in range(len(airportlist)+1):


                distance=airport.distanceBetweenAirports(routelist[j][k],routelist[j][k+1])
                totalroute+=distance

                if routelist[j][k]==routelist[j][k+1]:
                    control=1

                if distance>aircraftrange:# refuel enough to complete this leg


                    where=airport.getAirportCountry(routelist[j][k])
                    iseuro=countrycurr.getCurrencyCode(where)
                    currrate=currencyrate.getCurrencyRate(iseuro)
                    if distance<initialaircraftrange:
                       tobefueledopt=distance-aircraftrange
                       costopt=tobefueledopt*currrate
                       aircraftrange+=tobefueledopt
                       totalcostopt+=costopt


                if distance>aircraftrange: #still distance is bigger than range even when gas tank is full
                    control=1 #if control is 1 bestroute and cheapest is not calculated

                indx+=1

                aircraftrange=aircraftrange-distance

            totalroute1=totalroute
            aircraftrange=initialaircraftrange


            if control == 0:

#=======================COMPARING======================
                if mincost>totalcostopt:
                    mincost=totalcostopt
                    cheapestroutelist=routelist[j]
                    routedist=totalroute1
#==================================================

            else:
                impossible_routes_distancefuel.append(routelist[j]) # for counting impossible routes
                bestroutelist=0
                totalroute=0
                cost1=0

        if len(impossible_routes_distancefuel)==24:
            cheapestroutelist=0
            mincost=10**10
            routedist=0
            return cheapestroutelist,mincost,routedist,impossible_routes_distancefuel
        else:
            return cheapestroutelist,mincost,routedist,impossible_routes_distancefuel

