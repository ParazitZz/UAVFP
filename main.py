from Classes import *



if __name__ == "__main__":
    m = createMap()
    grid = D3Grid(hmap = m)
    grid.addUAV()
    grid.UAV.where()
    grid.UAV.moveTo(1,0)
    grid.UAV.where()
    grid.showGrid()