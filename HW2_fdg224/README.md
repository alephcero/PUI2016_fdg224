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

