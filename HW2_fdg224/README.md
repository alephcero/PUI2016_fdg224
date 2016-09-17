#Homework No2



##Assigment 1

**Script:** `show_bus_locations.py`

The script reports for every bus on a bus line, their current position with lat and long.

For the execution of the script:

```
python show_bus_locations.py <MTA_KEY> <BUS_LINE>
```

Personal MTA KEY and Bus line are taken from the terminal input with sys.argv. For the MTA KEY, an enviromental variable was used in the execution of the command like so: ` $MTAKEY ` 


**Tasks:**

* Created enviromental variable with my MTAKEY
* Defined two funcions:

⋅⋅⋅ *getBusList()* : takes a parsed input as given by the MTA API for a single busline and returns a list of buses, where every element of a list is the VehicleActivity of the bus.

⋅⋅⋅ *busLocation()* : takes the VehicleActivity of a bus (in dictionary format) and returns its latitude of longitude

##Assigment 2

**Script:** `get_bus_info.py`

The script reports for every bus on a bus line, their current position with lat and long, along with the next stop.

```
python get_bus_info.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv
```

**Tasks:**

On top of the task for the **Assigment 1**:

* Create two functions :

⋅⋅⋅ *busStopName()* : takes a VehicleActivity of a bus (in dictionary format) and returns its stop name.

⋅⋅⋅ *busStopStatus()* : takes a VehicleActivity of a bus (in dictionary format) and returns its stop status.


##Assigment 3

**File:** `HW2_3_fdg224.ipynb`

The Jupyter Notebook checks if a Enviromental Variable is declared by printin it, reads a CSV file from the CUSP Data Facility for NYS Math Test Results between 2006 and 2011, select columns for "Number of student tested" and "Mean Scale Score", and plot them. An hypothesis for the graph could be to check wether the size of the school (using the Number of student tested as a proxy) as a relation with the performance of the students in the test.

### Extra credit

**File:** `HW2_3_fdg224.ipynb`

In the same file, dates of the results are parsed in order to format the values properly as years. Then only English Proficent Schools and 8 graders are selected. Finally, a plot is rendered showing improvement of the mean score for each Borough 
