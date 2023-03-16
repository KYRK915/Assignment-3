"""
gathers building infor and number of sensors
"""
from sensorInfo import IotSensors

class building:

    def createSensors():
        buildName = input("Enter Building Name: ")
        noOfSensors = int(input("Enter the number of sensors deployed across Sheridan Campus: "))
        noOfSensors += 1
        sensor = 1

        while sensor != noOfSensors:
            print ("Sensor", sensor)
            sensor += 1

            IotSensors.sensorReadings()
            
        print (buildName)