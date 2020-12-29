import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def createMap(l=10, w=10, h=10):
    arr = np.zeros((l, w))
    for i in range(l):
        for j in range(w):
            if i != 0:
                if j != 0:
                    val = np.round(np.random.normal((arr[i, j-1] + arr[i-1, j]) / 2, scale=0.8), 1)
                else:
                    val = np.round(np.random.normal(arr[i-1, j], scale=0.8), 1)
            else:
                if j != 0:
                    val = np.round(np.random.normal(arr[i, j-1], scale = 0.8), 1)
                else:
                    val = 3
            if val >= 9:
                val = 8.5
            if val <= 0 :
                val = 1
            arr[i, j] = val
    return arr

class D3Grid():
    """
    Grid object in which UAVs will perform.
    """

    def __init__(self, x=10, y=10, z=10, hmap=createMap()):
        self.length = x
        self.width = y 
        self.height = z
        self.hmap = hmap
        # Create matrix for height map

    def showGrid(self):
        x, y = np.meshgrid(range(self.hmap.shape[0]), range(self.hmap.shape[1]))
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, self.hmap)
        plt.title('z as 3d height map')
        plt.show()
        plt.close()

    
    def addUAV(self, x=0, y=0, z=0):
        """
        Add an UAV. Class supports only one UAV for now.
        """
        self.UAV = UAV(self, x, y, self.hmap[x, y])

    def verifyCell(self, x, y):
        """
        Method to Check if a cell is contained in the grid
        """
        if (x >= 0 and x <= self.length - 1) and (y >= 0 and y <= self.width - 1): 
            return True
        else:
            return False
    

class UAV():

    def __init__(self, ParentGrid, x, y, z):
        self.ParentGrid = ParentGrid
        
        if self.ParentGrid.verifyCell(x, y):
            self.x = x
            self.y = y
            self.z = z
        else:
            print("Trying to instantiate UAV outside the Parent Grid")
            exit(-1)

    def moveTo(self, x, y):
        # Add check for distance, impossible zones, above floor
        if self.ParentGrid.verifyCell(x, y):
            self.x = x
            self.y = y
            self.z = self.ParentGrid.hmap[x, y] + 1
        else:
            print("Trying to move UAV outside the Parent Grid")
            exit(-1)

    def where(self):
        print(f"UAV is at ({self.x}, {self.y}, {self.z}).")
    
