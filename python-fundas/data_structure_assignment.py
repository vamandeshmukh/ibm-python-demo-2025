
# python data-structure-assignment.py

# Use infinite loop for user interaction
# Create a list of all the drivers 
# Add a driver to the above list 
# Print out the active drivers
# Search drivers in this area
# Sort drivers as per their locations
# Remove drivers inactive for more than a week. 
# Categirize drivers based on cars 

# data -  id, name (Full Name), car, car type (sedan, hatchback, suv), status (active / inactive), location (Location Name) 
#  validation for incoming values and search values 

drivers = [
    {"id": 101, "name": "Sonu Reddy", "car": "Dezire", "location": "Abids", "status": "active"},
    {"id": 102, "name": "Monu Singh", "car": "Ertiga", "location": "Hitechcity", "status": "active"},
    {"id": 103, "name": "Tonu Sharma", "car": "Swift", "location": "Secunderabad", "status": "active"},
    {"id": 104, "name": "Raju Kumar", "car": "WagonR", "location": "Uppal", "status": "inactive"},
    {"id": 105, "name": "Amit Verma", "car": "Ertiga", "location": "Abids", "status": "active"},
    {"id": 106, "name": "Vikram Das", "car": "Dzire", "location": "Koti", "status": "active"},
    {"id": 107, "name": "Suresh Patel", "car": "Ertiga", "location": "ECIL", "status": "inactive"},
    {"id": 108, "name": "Rajesh Yadav", "car": "Zest", "location": "Ramaplly", "status": "active"},
    {"id": 109, "name": "Manoj Jain", "car": "Baleno", "location": "Hitechcity", "status": "active"},
    {"id": 110, "name": "Kiran Rao", "car": "XUV", "location": "Koti", "status": "active"}
]

def addNewDriver(driver):
    drivers.append(driver)
    print("New driver added successfully!")

def getActiveDrivers():
    activeDrivers = []
    for driver in drivers:
        if driver["status"] == "active":
            activeDrivers.append(driver)
    return activeDrivers

def getNearbyDrivers(location):
    nearbyDrivers = []
    for driver in drivers:
        if driver["location"] == location:
            nearbyDrivers.append(driver)
    return nearbyDrivers


print("Total drivers ")
print(len(drivers))

print("Add new driver:")
newDriver = {
    "id": 111,
    "name": "Anil Kumar",
    "car": "Creta",
    "location": "Charminar",
    "status": "active"
}
addNewDriver(newDriver) 

print("Find nearby drivers:")
for driver in getNearbyDrivers("Koti"):
    print(driver["name"]) 
            
print("Active drivers:")
for driver in getActiveDrivers():
    print(driver["name"]) 



# list 
# drivers.
len(drivers)



myDriver = {"id": 101, "name": "Sonu Reddy", "car": "Dezire", "location": "Abids", "status": "active"}
# myDriver.

mySet = {1, 2, 3}
# mySet.
myVals = (1, 2, 3)
# myVals.