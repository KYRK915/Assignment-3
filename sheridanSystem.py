"""
This program creates the number of buildings
"""
from buildingInfo import building

class sheridanSystems:
    #starts the program
    def run():

        noOfBuild = input("Enter the number of buildings: ")
        builds = 1

        #checks if input is an integer
        if noOfBuild.isdigit():
            x = int(noOfBuild)
            x += 1 
            while builds != x:
                print ("Building", builds)
                building.createSensors()
                builds += 1 

        else:
            while noOfBuild.isdigit() == False:
                noOfBuild = input ("Re-enter the number of buildings: ")
                if noOfBuild.isdigit():
                    x = int(noOfBuild)
                    x += 1  
                    while builds != x:
                        print ("Building", builds)
                        building.createSensors()
                        builds += 1
            
            
        
    
    