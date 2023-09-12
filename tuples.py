"""a=("blaack","blue","green","red")
print(a)
#unpacking
(f,g,h,j)=a
print(f)

m="hey","hii",89
m[0]="hio"""

"""for t in enumerate("qwertyui"):
    index,character=t
    print(index,character)
"""
albums=[("a","b",1),
        ("c","d",2),
        ("e","f",3),]
print(len(albums))

#for album in albums:
 #   print("album:{0}, name:{1}, year:{2}".format(album[0],album[1],album[2]))

for name,artist,year in albums:
    print("album:{0}, name:{1}, year:{2}".format(name,artist,year))

    #or we can use 
    # for album in albums:
       # name,artist,year =albums
    #print("album:{0}, name:{1}, year:{2}".format(name,artist,year))
