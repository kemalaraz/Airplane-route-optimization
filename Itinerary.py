# -*- coding: utf-8 -*-


class Itinerary:

    """
    stores all the information of the given Itinerary and returns all needed
    information with functions
    """


    def __init__(self,cheapestroutelist,mincost,cheapestroutedist,shortestroutelist,shortestroutecost,shortestroutedist,aircraft):

        self.cheapestroutelist=cheapestroutelist
        self.mincost=mincost
        self.cheapestroutedist=cheapestroutedist
        self.shortestroutelist=shortestroutelist
        self.shortestroutecost=shortestroutecost
        self.shortestroutedist=shortestroutedist
        self.aircraft=aircraft

    def getCheapestRouteList(self):
        return self.cheapestroutelist

    def getMinCost(self):
        return self.mincost

    def getCheapestRouteDist(self):
        return self.cheapestroutedist

    def getShortestRouteList(self):
        return self.shortestroutelist

    def getShortestRouteCost(self):
        return self.shortestroutecost

    def getShortestRouteDist(self):
        return self.shortestroutedist

    def getAircraft(self):
        return self.aircraft
