#Run a simple data query

import pandas as pd
df = pd.read_excel('south-africa-statistics.xlsx', sheet_name=0)
df.iloc[0]

#The statistics range from year 1960 - 2021

import numpy as np
import pandas as pd
df = pd.read_excel('south-africa-statistics.xlsx', sheet_name=0)
x = df.iloc[0]
y = df.iloc[1]
arr_x = np.array(x)
arr_y = np.array(y)
for z in range (4, 66):
print(arr_x[z])

#Theres 65 values/columns in each row (but start at index 4)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_excel('south-africa-statistics.xlsx', sheet_name=0)
x = df.iloc[0]
arr = np.array(x)
print(arr[4:66])

#GDP per Capita

import numpy as np
import pandas as pd
df = pd.read_excel('south-africa-statistics.xlsx', sheet_name=0)
x = df.iloc[0] #years
y = df.iloc[1080]
arr_x = np.array(x)
arr_y = np.array(y)
#print(arr_x[4:66])
#print(arr_y[4:66])
plt.title("GDP per capita (current US$)")
plt.xlabel("Years")
plt.ylabel("")
plt.plot(arr_x[4:66], arr_y[4:66])
plt.show()

#Travel services (% of commercial service exports)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_excel('south-africa-statistics.xlsx', sheet_name=0)
x = df.iloc[0] #years
y = df.iloc[1]
arr_x = np.array(x)
arr_y = np.array(y)
#print(arr_x[4:66])
#print(arr_y[4:66])
plt.plot(arr_x[4:66], arr_y[4:66])
plt.show()

