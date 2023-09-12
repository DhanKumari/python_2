data = [ 
    ("orange", " a sweet, orange, citrus fruit"),
    ("apple","good for making cider"),
    ("lemon","a sour, yellow citrus fruit"),
    ("grape","a small, sweet fruit growing in bunches"),
    ("melon","sweet and juicy")

]

#print(ord("a"))
#print(ord("b"))
#print(ord("z"))
"simple hash function "
def simple_hash(s:str)->int:  #passing a string it returns int 
    basic_hash = ord(s[0])
    return basic_hash % 10

"""
for key, value in data:
    #h = simple_hash(key)  #gives one fixedd value  
    h=hash(key) #python hhhash function codes r different 
    print(key, h)
    
    """
def get(k: str)-> int:
    "return the value for key or none if doesnt exist"
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None

    
    
keys = [""]*10
values = keys.copy()  #copy of list

for key, value in data:
    h = simple_hash(key)
    print(key,h)
    keys[h] = key     #replacing the empty string with key or value  
    values[h] = value
    
print(keys)
print(values)
print()
value = get("grape")
print(value)

 
    

    