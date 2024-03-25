import netCDF4
import pandas as pd

class DataParser:
    def __init__(self, fileName) -> None:
        self.fileName = fileName
        self.nc = netCDF4.Dataset(fileName)

    def printKeys(self):
        print(self.nc.variables.keys())

    def getVariable(self, key):
        try: 
            return self.nc.variables[key]
        except:
            return None
    
    def createDataFrame(self, keys):
        df = pd.DataFrame()
        for key in keys:
            df.assign(key = lambda x: self.getVariable(key))
        return df