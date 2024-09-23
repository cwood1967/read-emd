### read-emd
Simple talos emd file reader for python.

### Installation
```
pip install git+https://github.com/cwood1967/read-emd
```

### Example

```python
# import the EmdReader class
from reademd import EmdReader

# create a reader with the path to an emd file
emdfile = "mydata.emd"
data = EmdReader(emdfile)

# read the image and get the pixel size
image = e.readImage(idx=0)
py, px = e.getPixelSize(idx=0)

# retreive all the metadata in a dictionary
metadata = e.readMetaData(idx=0)
```