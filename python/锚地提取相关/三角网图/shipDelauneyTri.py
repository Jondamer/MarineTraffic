
import numpy as np
from scipy.spatial import Delaunay
import math
# from geoplotlib.utils import read_csv, BoundingBox
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
import pandas as pd
import os
import os.path

# JSON data from the gist above.
##coordinates = [f['geometry']['coordinates'] for f in json.loads(data)]
##points = np.array(coordinates)

data = pd.DataFrame()
# bohaiFiles = 'bohai_youshang_TankerShips/'
# bohaiFiles = 'D:/航海项目/data/'
nanhaiFiles='D:/航海项目数据/停留点数据/'
# bohaiFiles = 'D:\\PYWorkSpace\\三角网\\bohai_youshang_TankerShips'
for parent, dirnames, filenames in os.walk(nanhaiFiles):
    for filename in filenames:
        print(nanhaiFiles + filename)
        data = data.append(pd.read_csv(nanhaiFiles + filename, header=None))
x, y = data[1], data[2]
points = np.array(list(set(zip(x, y))))

# print (points)

tri = Delaunay(points)

plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o', color='red')
plt.show()
