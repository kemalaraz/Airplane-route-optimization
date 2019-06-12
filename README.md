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
Attributes
 Airport_id: ID of the airport \n
 Name: Name of the airport
 City: Cities that an airport located in
 Code: 3 letter IATA code of the airport
 Ica code: 4 letter ICA code of the airport
 Lat: Latitude of the location that airport is located
 Long: Longitude that the airport is located in
 Alt: Altitude of the airport
 Toffset: Timezone offset
 DST: Daylight saving time
 Tz: timezone
Methods
 getCoordinates():A method that returns the latitude and longitude of given airport.
 getCountry(): Returns the country of the given airport
2. AirportAtlas: Opens airport.csv file and sends the information contained in that file to airport class also have some other methods.
Attributes
 Airportdict: A dictionary that holds the information about airports with IATA key.
Methods
 loadData():A method that opens airport.csv file, assigns them to a dictionary and sends them to airport class.
 getAirportCountry ():A method that takes the IATA code and send the address of it to airport class for bringing the airport country.
 greatCircleDist(): Takes the latitude and longitude of two airports and return the great circle distance between them
 distanceBetweenAirports(): Takes two IATA codes as input sends them to get coordinates(lat and long) after that sends those to greatCircleDist to get the distance, then sends it back where it is requested
3. Aircraft: Stores information about the aircrafts.
Attributes
 Code: Name of the aircraft
 Types: Type of the aircraft

