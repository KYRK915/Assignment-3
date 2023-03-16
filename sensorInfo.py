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
                z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) :".format(days))
                

                # This makes sure the input is between 20 and 50
                if z.isdigit():
                    k = int(z)
                    if k >= 20 and k <= 50:
                        aveList.append(k)
                    elif k <20 or k >50:
                        while k <20 or k >50:
                            print ('Wrong Input')
                            z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                            k = int(z)
                            if k >= 20 and k <= 50:
                                aveList.append(k)
                                
                else:
                    while z.isdigit() == False:
                        print ('Wrong Input')
                        z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                        if z.isdigit():
                            k = int(z)
                            if k >= 20 and k <= 50:
                                aveList.append(k)
                            elif k <20 or k >50:
                                while k <20 or k >50:
                                    print ('Wrong Input')
                                    z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                                    z = int(k)
                                    if k >= 20 and k <= 50:
                                        aveList.append(k)
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
                        z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))

                        # This makes sure the input is between 20 and 50
                        if z.isdigit():
                            k = int(z)
                            if k >= 20 and k <= 50:
                                aveList.append(k)
                            elif k <20 or k >50:
                                while k <20 or k >50:
                                    print ('Wrong Input')
                                    z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                                    k = int(z)
                                    if k >= 20 and k <= 50:
                                        aveList.append(k)
                                
                        elif z.isdigit() == False:
                            while z.isdigit() == False:
                                print ('Wrong Input')
                                z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                                if z.isdigit():
                                    k = int(z)
                                    if k >= 20 and k <= 50:
                                        aveList.append(k)
                                    elif k <20 or k >50:
                                        while k <20 or k >50:
                                            print ('Wrong Input')
                                            z = input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ".format(days))
                                            k = int(z)
                                            if k >= 20 and k <= 50:
                                                aveList.append(k)
                days += 1 
                
                computeAvg()


    
    