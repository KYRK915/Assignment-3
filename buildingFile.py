"""
gathers building infor and number of sensors
"""


class building:

    buildingList = []
    
    def printInfo():
        import IotSensorFile
        import sheridanSystemFile
        sensors = 1
        builds = 1
        days = 1 
        d = int(sheridanSystemFile.sheridanSystems.sheridanSystemsList[0])
        d += 1
        e = int (building.buildingList[1])
        e += 1 
        f = int (IotSensorFile.IotSensors.IotSensorsList[2])
        f += 1 
        g = ''
        h = []
        if len (IotSensorFile.IotSensors.IotSensorsList) == 5:
            h.append(IotSensorFile.IotSensors.IotSensorsList[3])
        elif len (IotSensorFile.IotSensors.IotSensorsList) > 5:
            for j in (IotSensorFile.IotSensors.IotSensorsList[3:5]):
                h.append(j)
               
        while builds != e:
            print ('This is for Building: ' + building.buildingList[0])
            builds += 1
            while sensors != d:
                print ('Sensor', sensors)
                sensors += 1
                print ('x:', IotSensorFile.IotSensors.IotSensorsList[0])
                print ('y:', IotSensorFile.IotSensors.IotSensorsList[1])
                while days!= f:
                    for g in h:
                        print ('Day', days, g,'PPM')        
                    days+=1
                print('Average Reading(s): ', IotSensorFile.IotSensors.IotSensorsList[-1])
                
        
    def createSensors():
        import IotSensorFile
        buildName = input("Enter Building Name: ")
        if (buildName.isnumeric() == False) and (len(buildName) == 10):
            building.buildingList.append(buildName)
            noOfSensors = input("Enter the number of sensors deployed across Sheridan Campus: ")           
            if noOfSensors.isdigit():
                building.buildingList.append(noOfSensors)
                a = int(noOfSensors)  
                a +=1
                sensors = 1
                while sensors != a:
                    print('Sensor', sensors)
                    sensors += 1
                    IotSensorFile.IotSensors.sensorReadings()
                    
            
            else:
                while noOfSensors.isdigit() == False:
                    noOfSensors = input("Enter the number of sensors deployed across Sheridan Campus: ")
                    if noOfSensors.isdigit():
                        building.buildingList.append(noOfSensors)
                        a = int(noOfSensors)  
                        a +=1
                        while sensors != a:
                            print ("Sensor", sensors)
                            sensors += 1
                            IotSensorFile.IotSensors.sensorReadings()
        
        else:
            while (buildName.isnumeric()==False) or (len(buildName)!= 10):
                print ("Invalid Entry")
                buildName = input("Re-Enter Building Name: ")
                if (buildName.isnumeric() == False) and (len(buildName) == 10):
                    building.buildingList.append(buildName)
                    noOfSensors = input("Enter the number of sensors deployed across Sheridan Campus: ")
                    sensors = 1           
                    if noOfSensors.isdigit():
                        building.buildingList.append(noOfSensors)
                        a = int(noOfSensors)  
                        a +=1
                        while sensors != a:
                            print ("Sensor", sensors)
                            sensors += 1
                            IotSensorFile.IotSensors.sensorReadings()
            
                    else:
                        while noOfSensors.isdigit() == False:
                            ("Enter the number of sensors deployed across Sheridan Campus: ")
                            if noOfSensors.isdigit():
                                building.buildingList.append(noOfSensors)
                                a = int(noOfSensors)  
                                a +=1
                                while sensors != a:
                                    print ("Sensor", sensors)
                                    sensors += 1
                                    IotSensorFile.IotSensors.sensorReadings()
    