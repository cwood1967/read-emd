import json

import numpy as np
import h5py

class EmdReader:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.f = h5py.File(self.filepath, 'r')
        self.metadata = dict() 
        self.getImageKeys()

    def getImageKeys(self):
        keys = list(self.f['Data']['Image'].keys())
        self.imagekeys = keys
        
    def readMetadata(self, idx=0):
        key = self.imagekeys[idx]
        md = self.f['Data']['Image'][key]['Metadata']
        sx = [chr(i[0]) for i in md]
        s = "".join(sx)
        s0 = s.split("\n\x00")[0]
        js = json.loads(s0)
        self.metadata[idx] = js
        return js
        
    def getPixelSize(self, idx=0):
        if idx not in self.metadata:
            md = self.readMetadata(idx=idx)
        
        pixelsize = md['BinaryResult']['PixelSize']
        px = float(pixelsize['width'])*1e9
        py = float(pixelsize['height'])*1e9
        return py, px
        
    
    def readImage4(self, idx=0):
        key = self.imagekeys[idx]
        x = np.array(self.f['Data']['Image'][key]['Data'])
        x = np.squeeze(x)
        return x
    
        

