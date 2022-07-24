import os
import csv
from xmlrpc.client import Boolean

import numpy as np

class csv_service():
    def __init__(self) -> None:
        self.name = 'output.csv'
        self.path = './'

    def setFilePath(self, path) -> None:
        self.path = path

    def setFileName(self, name) -> None:
        self.name = name + '.csv'

    def readCSV(self) -> None:
        print('aa')
    
    def writeCSV(self, data) -> Boolean:
        
        f = open(self.path + self.name, 'w', encoding='utf-8', newline='')
        write = csv.writer(f)
        print(data)
        try:
            if data.shape[1] == NULL :
                #data = np.arrange(data)
                #print(data)
                #np.savetxt(self.path + self.name, data, delimiter=",")
                write.writerow(data)
            else :
                print(data)
                write.writerows(data)
        except Exception as e:
            print(e)
            f.close()
            return False
        f.close()
        return True
    
    