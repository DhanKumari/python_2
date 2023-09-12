data=[4,5,104,105,110,120,130,130,150,160,170,183,185,
      187,188,191,350,360]


min_v=100
max_v=200
stop=0
print(data)

"""for index,value in enumerate(data):
    if (value<min_v)or (value>max_v):
        del data[index]
print(data)"""

#process the low values 
for index, value in enumerate(data):
    if value>=min_v:
        stop =index
        break
print(stop)
del data[:stop]
print(data)


#process the high values , -1 is used coz last value will not be included ohtewise 
start=0
for index in range(len(data)-1,-1,-1):
    if data[index]<=max_v:
        start=index+1 #coz we dont want to delete value of index 13
        break
print(start)
del data[start:]
print(data)





#iterating backwards 
"""for index in range(len(data)-1,-1,-1):
    if data[index]<=max_v:
        stop =index
        break
print(data)"""
    