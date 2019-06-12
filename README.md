# Airplane-route-optimization


## 1. A brief summary
This program is designed to find shortest and cheapest routes of an airplane that is doing five trips each week. It takes parameters from a GUI which are one home airport and four other airports that the plane will stop during its route and finally an aircraft type from a given list. After that it calculates shortest route and cheapest route and display the results.
This program needs additional documents to execute which are;
- Airport.csv: Contains information about all the airports around the world.
- Aircraft.csv: Contains information about some aircrafts
- Countrycurrency.csv: Contains information about currencies about countries
- Currencyrates.csv: Contains information about the rates between euro and other currencies

## 2. Information about Interface
There is a screenshot of the initial interface the program has when it is opened shown below. Below Home Airport text user can input the IATA code of the home airport which the aircraft depart from and return for the end of the route. Below that there are four airport input widgets that user can type the IATA codes of the airports that aircraft will fly to. Near that widgets there is a list box which user can click on the aircraft that will conduct that specified route. After typing airports IATA codes and deciding the aircraft type user can click submit for displaying the results which are shortest and cheapest routes calculated by calculations which will described in sections below. Also after displaying the results user can write these results to a csv file which is called bestroute.csv.

![](images/UI_snap.JPG)

## 3. Program Overview
### 3.1. Class Explanations
#### 1. Airport: Stores information about the airports that airport.csv file.
##### Attributes <br />
- Airport_id: ID of the airport <br />
- Name: Name of the airport <br />
- City: Cities that an airport located in <br />
- Code: 3 letter IATA code of the airport <br />
- Ica code: 4 letter ICA code of the airport <br />
- Lat: Latitude of the location that airport is located <br />
- Long: Longitude that the airport is located in <br />
- Alt: Altitude of the airport <br />
- Toffset: Timezone offset <br />
- DST: Daylight saving time <br />
- Tz: timezone <br />
##### Methods
- getCoordinates():A method that returns the latitude and longitude of given airport <br />
- getCountry(): Returns the country of the given airport <br />
#### 2. AirportAtlas: Opens airport.csv file and sends the information contained in that file to airport class also have some other methods
##### Attributes <br />
- Airportdict: A dictionary that holds the information about airports with IATA key.
##### Methods
- loadData():A method that opens airport.csv file, assigns them to a dictionary and sends them to airport class.
- getAirportCountry ():A method that takes the IATA code and send the address of it to airport class for bringing the airport country.
- greatCircleDist(): Takes the latitude and longitude of two airports and return the great circle distance between them
- distanceBetweenAirports(): Takes two IATA codes as input sends them to get coordinates(lat and long) after that sends those to greatCircleDist to get the distance, then sends it back where it is requested
#### 3. Aircraft: Stores information about the aircrafts.
##### Attributes
- Code: Name of the aircraft
- Types: Type of the aircraft
- Units: Represent the range of the aircraft (if it is metric than range is shown by km, if it is imperial than the range s shown by miles.
- Manu: Manufacturer of aircraft.
- Ranges: Range of the aircraft.
###### Methods
- metric():A method that checks whether unit of the aircraft is imperial, if it is changes it to km.
- getAircraftRanges(): Returns the range of an aircraft.
#### 4. AircraftList: Opens aircraft.csv, sends that information to aircraft class also have some other methods.
##### Attributes
- AircraftDict: A dictionary that holds information about aircrafts and the key is its name.
##### Methods
- loadData():A method that opens aircraft.csv file, assigns them to a dictionary and sends them to aircraft class.
- getAircraftRanges(): Takes the name of aircraft and with the help of the dictionary sends the address of it to airport class which returns the range of an aircraft and send that value to where it requested.
5. Currency: Stores information from currency.csv.
##### Attributes
- Countryname: Holds the currency’s country name
- Code: Currency code
- Currencyname: Holds currencyname
##### Methods
- Currencycode():A method that returns currency’s code.
#### 6. CurrencyList: Opens currency.csv and assigns the information to a dictionary and sends them to currency class.
##### Attributes
- Currencydict: Holds the information about the currency with a key of countryname.
##### Methods
- getCurrencycode(): A method that takes the dictionary key and sends the address to currency for returning requested data.
##### 7. CurrencyRate: Stores information from currencyrate.csv.
###### Attributes
- Currencyname: Holds the currency’s country name 
- Code: Currencyrate code
- Exchangerate: Holds exchange rate with euro
##### Methods
- getCurrencyRate():A method that returns currency’s exchangerate.
#### 8. CurrencyRateList: Opens currencyrates.csv and assigns the information to a dictionary and sends them to currencyrate class.
##### Attributes
- Currencyratedict: Holds the information about the currencyrate with a key currencycode.
##### Methods
- getCurrencyRate(): A method that takes the dictionary key and sends the address to currencyrate for returning requested data.
#### 9. Itinerary: Stores information about the itineries and sends back information when needed.
##### Attributes
- Cheapestroutelist: Stores cheapest route list.
- Mincost: Stores the minimum cost that is found via calculation.
- Cheapestroutedist: Stores cheapest route distance.
- Shortestroutelist: Stores shortest route list.
- Shortestroutecost: Stores shortest route cost found via calculation.
- Shortestroutedist: Stores shortest route distance.
- Aircraft: Stores aircraft name.
##### Methods
- getCheapestRouteList (): Returns cheapest route list.
- getMinCost(): Returns minimum cost.
- getCheapestRouteDist(): Returns cheapest route distance.
- getShortestRouteList(): Returns shortest route list.
- getShortestRouteCost(): Returns shortest route cost.
- getShortestRouteDist(): Returns shortest route distance.
- getAircraft(): Returns selected aircraft name.
#### 10. ItineraryList: Most important class in the program. Has a method call in __init__ that calls loadData to populate itinerary class with attributes but before that does the calculation for finding cheapest and shortest route.
##### Methods
- getCheapestRouteList (): Returns cheapest route list.
- getMinCost(): Returns minimum cost.
- getCheapestRouteDist(): Returns cheapest route distance.
- getShortestRouteList(): Returns shortest route list.
- getShortestRouteCost(): Returns shortest route cost.
- getShortestRouteDist(): Returns shortest route distance.
- getAircraft(): Returns selected aircraft name.
- permutations(): Finds all the permutations between departing from home and returning it.
- calculationForFiveRoutes(): Has two method calls inside for calculations so it takes its solutions which are shortest and cheapest route by refueling whole tank and the other is calculating cheapest route(which also gives shortest) refueling enough for completing specified leg.(second one is a little optimization)
- Fullrefuel(): Finds cheapest and shortest route by refueling whole tank
- Distancerefuel(): Finds cheapest route by refueling just enough for completing the leg.
#### 11. Main_code: It is dedicated for GUI has a a lot of attributes for constructing the interface and some methods.
##### Methods
- addToListandDisplay ():For adding the user inputs to a list and displaying the result.
- writeToCsv (): Writes result to csv file.

### 3.2. Class Diagram

![](images/Class_Diagram.JPG)

## 4. Shortest and Cheapest Routes
First program takes parameters from the user as discussed above then checks for errors. After that sends those parameters to itinerartlist class. This class first separates airports from aircraft then sends them to calculateForFiveRoutes method. After that this list of airports sended to permutations method for finding all permutations of this list however after going into that method homeairport pops out then without the home airport all possible routes are found. Later home airport is appended to the first and last index of that list. Then list returns back to calculationForFiveRoutes method which sends it to the fullrefuel with airportlist and aircraftcode. Fullrefuel method first opens the files that mentioned above for taking the data and then with getaircraftrange() method gets back the range of that particular aircraft. Later with for inside for first calculates the distance between two airports by distanceBetweenAirports method and adds it to totalroute. Later if routelist[j][k]==routelist[j][k+1] checks whether two airports are the same if so it assigns control to one for skipping comparing. After that checks whether the distance is bigger than aircraftrange. At beginning it doesn’t do much but when the aircrafts fuel began to decrease it goes inside that if and then subtracts the initialaircraftrange from aircraftrange that remains for refueling. Then gets the country from airport class, takes that country and sends it to currency class for getting currencycode and takes it sends it to currencyrate class for getting exchangerate for refueling. Calculates the cost and adds it to the totalcost. Then with another if checks whether the distance is still bigger than range if that is so the route is impossible and calculations will done later shouldn’t be done so it assigns control to 1 that will checked by a if later and if it is zero another if checks whether this routes distance is smaller than distances before if so it assigns that toute to permanent variable and its list and cost too. It does same thing for cheapest route also. By the way if control is one none of it happens and it appends that route to impossible_routes_fullrefuel and if it is 24(all possible routes) then there is no possible route for this problem. If there is even one it returns all important variables to calculateForFiveRoutes method. Then distancerefuel method is initiated. This method does the same thing except it refuels the aircraft only the distance to complete the leg. For example if aircraft has 1000km fuels and that leg is 3000km it only refuels 2000km. By doing this it makes shortest, equal to cheapest so returns only three variables(list,cost,distance). After that calculateForFiveRoutes compares the results that are taken from two methods and sends back the minimum to GUI. After that GUI compares and displays the results.

## 5. Testing
Generally I used try except function for detecting errors however I also have an extra file called ItinerartList_TEST.py and in that file I have print functions every for every step to see mistakes, errors and possible calculation mistakes. I used try except methods for opening files which is located in the itinerarylist method and also in the main_code when user try to type airport codes into the GUI and mistypes it detects the errors and pops up messageboxes for that also if user don’t select an aircraft it also brings up a messagebox some examples shown below. There are some imporvements should be made on the testing part as a future work.
