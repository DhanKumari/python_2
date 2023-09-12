from nested_tuples import albums
print(albums)


while True:
    print("please choose ur album:")
    for index,(title,artist,year,songs) in enumerate(albums):
        print("{}:{},{},{}".format(index+1,title,artist,year,songs))

"""
    for index,value in enumerate(albums):
        title,artist,year,songs=value
        print(index,title,artist,year,songs)
    break"""
