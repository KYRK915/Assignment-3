"""
This program creates the number of buildings
"""



class sheridanSystems:
    
    sheridanSystemsList = []
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
                import buildingFile
                sheridanSystems.sheridanSystemsList.append(builds)
                buildingFile.building.createSensors()
                builds += 1 
                

        else:
            while noOfBuild.isdigit() == False:
                noOfBuild = input ("Re-enter the number of buildings: ")
                if noOfBuild.isdigit():
                    x = int(noOfBuild)
                    x += 1  
                    while builds != x:
                        import buildingFile
                        print ("Building", builds)
                        sheridanSystems.sheridanSystemsList.append(builds)
                        buildingFile.building.createSensors()
                        builds += 1   
    
    