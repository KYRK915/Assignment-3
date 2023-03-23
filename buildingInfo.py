"""
gathers building infor and number of sensors
"""
from sensorInfo import IotSensors

class building:

    buildingList = []
    
    def createSensors():
        buildName = input("Enter Building Name: ")
        building.buildingList.append(buildName)
        if (buildName.isnumeric() == False) and (len(buildName) == 10):
            noOfSensors = input("Enter the number of sensors deployed across Sheridan Campus: ")
            sensors = 1           
            if noOfSensors.isdigit():
                a = int(noOfSensors)  
                a +=1
                while sensors != a:
                    print('Sensor', sensors)
                    sensors += 1
                    IotSensors.sensorReadings()
            
            else:
                while noOfSensors.isdigit() == False:
                    noOfSensors = input("Enter the number of sensors deployed across Sheridan Campus: ")
                    if noOfSensors.isdigit():
                        a = int(noOfSensors)  
                        a +=1
                        while sensors != a:
                            print ("Sensor", sensors)
                            sensors += 1
                            IotSensors.sensorReadings()
        
        else:
            while (buildName.isnumeric()==False) or (len(buildName)!= 10):
                print ("Invalid Entry")
                buildName = input("Re-Enter Building Name: ")
                if (buildName.isnumeric() == False) and (len(buildName) == 10):
                    noOfSensors = input("Enter the number of sensors deployed across Sheridan Campus: ")
                    sensors = 1           
                    if noOfSensors.isdigit():
                        a = int(noOfSensors)  
                        a +=1
                        while sensors != a:
                            print ("Sensor", sensors)
                            sensors += 1
                            IotSensors.sensorReadings()
            
                    else:
                        while noOfSensors.isdigit() == False:
                            ("Enter the number of sensors deployed across Sheridan Campus: ")
                            if noOfSensors.isdigit():
                                a = int(noOfSensors)  
                                a +=1
                                while sensors != a:
                                    print ("Sensor", sensors)
                                    sensors += 1
                                    IotSensors.sensorReadings()


        
            
        return buildName
    
    
    
    
        