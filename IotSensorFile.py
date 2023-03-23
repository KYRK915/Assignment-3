"""
gathers info for sensor position, CO2 readings and computes average
"""
import random

class IotSensors:

    IotSensorsList= []
    
    # asks the user for CO2 readings
    def sensorReadings():
        days = 1
        aveList = []
        
        
        # Gives the sensor positions
        def sensorPos():
            x = random.randint(1,100)
            y = random.randint(1,100)
            IotSensors.IotSensorsList.append(x)
            IotSensors.IotSensorsList.append(y)

        sensorPos()
    
        # computes the average CO2 reading
        def computeAvg():
            import buildingFile
            ave = sum(aveList)/ len(aveList)
            print("Rounded Average Readings", ave , 'PPM')
            IotSensors.IotSensorsList.append(ave)
            buildingFile.building.printInfo()             

        noDays = input("Enter the number of days for the readings: ")
        
        if noDays.isdigit():
            IotSensors.IotSensorsList.append(noDays)
            b = int(noDays) 
            b += 1
            

            #This asks the user for the CO2 readings based on how many days they input
            while days != b:
                z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) :".format(days))
                

                # This makes sure the input is between 20 and 50
                if z.isdigit():
                    k = int(z)
                    if k >= 20 and k <= 50:
                        aveList.append(k)
                        IotSensors.IotSensorsList.append(k)

                    elif k <20 or k >50:
                        while k <20 or k >50:
                            print ('Wrong Input')
                            z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days)))
                            if z >= 20 and z <= 50:
                                aveList.append(z)
                                IotSensors.IotSensorsList.append(z)
                                                              
                else:
                    while z.isdigit() == False:
                        print ('Wrong Input')
                        z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                        if z.isdigit():
                            k = int(z)
                            if k >= 20 and k <= 50:
                                aveList.append(k)
                                IotSensors.IotSensorsList.append(k)
                            elif k <20 or k >50:
                                while k <20 or k >50:
                                    print ('Wrong Input')
                                    z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days)))
                                    if z >= 20 and z <= 50:
                                        aveList.append(z)                 
                                        IotSensors.IotSensorsList.append(z)
                days += 1
                
            #This computes the average CO2 reading
            computeAvg()
        else:
            while noDays.isdigit() == False:
                noDays = input("Re-Enter the number of days for the readings: ")
                if noDays.isdigit():
                    IotSensors.IotSensorsList.append(noDays)
                    b = int(noDays) 
                    b += 1
                    days = 1
                    aveList = []

                #This asks the user for the CO2 readings based on how many days they input
                    while days != b:
                        z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))

                        # This makes sure the input is between 20 and 50
                        if z.isdigit():
                            k = int(z)
                            if k >= 20 and k <= 50:
                                aveList.append(k)
                                IotSensors.IotSensorsList.append(k)
                            elif k <20 or k >50:
                                while k <20 or k >50:
                                    print ('Wrong Input')
                                    z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days)))
                                    
                                    if z >= 20 and z <= 50:
                                        aveList.append(z)
                                        IotSensors.IotSensorsList.append(z)
                           
                        
                        elif z.isdigit() == False:
                            while z.isdigit() == False:
                                print ('Wrong Input')
                                z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                                if z.isdigit():
                                    k = int(z)
                                    if k >= 20 and k <= 50:
                                        aveList.append(k)
                                        IotSensors.IotSensorsList.append(k)
                                    elif k <20 or k >50:
                                        while k <20 or k >50:
                                            print ('Wrong Input')
                                            z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days)))                                           
                                            if z >= 20 and z <= 50:
                                                aveList.append(z)
                                                IotSensors.IotSensorsList.append(z)
                                        
                days += 1   
                return noDays
            computeAvg()

        
    
    
    