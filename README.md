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

