"""
gathers info for sensor position, CO2 readings and computes average
"""
import random


class IotSensors:

    # asks the user for CO2 readings
    def sensorReadings():

        # Gives the sensor positions
        def sensorPos():
            print ("x:", str(random.randint(1,100)))
            print ('y:', str(random.randint(1,100)))

        sensorPos()

        # computes the average CO2 reading
        def computeAvg():
            print("Rounded Average Readings", sum(aveList)/ len(aveList), 'PPM')


        noDays = input("Enter the number of days for the readings: ")
        
        if noDays.isdigit():
            b = int(noDays) 
            b += 1
            days = 1
            aveList = []

            #This asks the user for the CO2 readings based on how many days they input
            while days != b:
                z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ". format(days)))

                # This makes sure the input is between 20 and 50
                if z >= 20 and z <= 50:
                    aveList.append(z)
                elif z <20 or z >50:
                    while z <20 or z >50:
                        print ('Wrong Input')
                        z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ". format(days)))
                        if z >= 20 and z <= 50:
                            aveList.append(z)
                days += 1 

                computeAvg()
        


        else:
            while noDays.isdigit() == False:
                noDays = input("Re-Enter the number of days for the readings: ")
                if noDays.isdigit():
                    b = int(noDays) 
                    b += 1
                    days = 1
                    aveList = []

                #This asks the user for the CO2 readings based on how many days they input
                    while days != b:
                        z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ". format(days)))

                        # This makes sure the input is between 20 and 50
                        if z >= 20 and z <= 50:
                            aveList.append(z)
                        elif z <20 or z >50:
                            while z <20 or z >50:
                                print ('Wrong Input')
                                z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ". format(days)))
                                if z >= 20 and z <= 50:
                                    aveList.append(z)
                        days += 1 

                        computeAvg()


    
    