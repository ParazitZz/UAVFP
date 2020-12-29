class D3Grid():
    """
    Grid object in which UAVs will perform.
    """

    def __init__(self, x=10, y=10, z=10):
        self.length = x
        self.width = y 
        self.height = z
        # Create matrix for height map

    def addUAV(self, x=0, y=0, z=0):
        """
        Add an UAV. Class supports only one UAV for now.
        """
        self.UAV = UAV(self, x, y, z)

    def verifyCell(self, x, y, z):
        """
        Method to Check if a cell is contained in the grid
        """
        if (x >= 0 and x <= self.length - 1) and (y >= 0 and y <= self.width - 1) and (z >= 0 and z <= self.height - 1):
            return True
        else:
            return False


class UAV():

    def __init__(self, ParentGrid, x, y, z):
        self.ParentGrid = ParentGrid
        
        if self.ParentGrid.verifyCell(x, y, z):
            self.x = x
            self.y = y
            self.z = z
        else:
            print("Trying to instantiate UAV outside the Parent Grid")
            exit(-1)

    def moveTo(self, x, y, z):
        # Add check for distance, impossible zones, above floor
        if self.ParentGrid.verifyCell(x, y, z):
            self.x = x
            self.y = y
            self.z = z
        else:
            print("Trying to move UAV outside the Parent Grid")
            exit(-1)

    def where(self):
        print(f"UAV is at ({self.x}, {self.y}, {self.z}).")
    
grid = D3Grid()
grid.addUAV()
grid.UAV.moveTo(1,0,0)
grid.UAV.where()