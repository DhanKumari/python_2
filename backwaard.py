data=[104,101,4,105,308,5,107
      ,100,306,106,102,108]
min_v=100
max_v=200

"""for index in range(len(data)-1,-1,-1):
    if data[index] < min_v or data[index] > max_v :
        print(index,data)
        del data[index]
print(data)
    
"""
#reversed function 
real=len(data)-1
for index,value in enumerate(reversed(data)):
    if value<min_v or value>max_v:
        print(real-index, value)
        del data[real-index]
print(data)

