"""
This runs the program
"""

from sheridanSystem import sheridanSystems
from buildingInfo import building

class Application:

    def start ():
        print ("program has started")

        sheridanSystems.run()


    start()