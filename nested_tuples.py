albums=[("a","b",11,
        [( 1,"aaa"),
          (2,"bbbb" ),
          ]
          ),

        ("c","d",22,
         [( 1,"ccc"),
          (2,"ddd")
          ]),
        ("e","f",33,
        [( 1,"eee"),
          (2,"hhhh" )
          ]
          ),
          
          ]
"""
for name,artist,year,songs in albums:
    print("album:{0}, name:{1}, year:{2},song:{3}".format(name,artist,year,songs))

print()

album=albums[2]
print(album)

song=album[2]
print(songs)

song=songs[1]
print(song)
print(song[1])
print()
mayhem=albums[2][2][1][1]
print(mayhem)


"""





