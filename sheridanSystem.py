"""
This program creates the number of buildings
"""
from buildingInfo import building

class sheridanSystems:
    
    def run():
        noOfBuild = input("Enter the number of buildings: ")
        print (type(noOfBuild))
        builds = 1


        if noOfBuild.isdigit():
            x = int(noOfBuild)
            x += 1 
            while builds != x:
                building.createSensors()
                builds += 1 

        else:
            while noOfBuild.isdigit() == False:
                noOfBuild = input ("Re-enter the number of buildings: ")
                if noOfBuild.isdigit():
                    x = int(noOfBuild)
                    x += 1  
                    while builds != x:
                        building.createSensors()
                        builds += 1
            
            
        
    
    