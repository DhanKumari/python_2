
class Song:
    """class to represent a song 
    
    attributes: 
    title (str): the title of the song 
    artist(str): name of the songs creator.
    duration(int): the duration of the song in seconds. may be zerp
    """
    def __init__(self, title, artist, duration = 0):
      
        self.title = title
        self.artist = artist
        self.duration = duration
        
    def get_title(self):
        return self.title
    
    name= property(get_title)
        
class Album:
    """class to represent songs albums 
    
    attributes: 
    name (str): the title of the song 
    year(int): an artist object represnting the songs creator.
    track(list[Song]): a list of songs 
    
    method:
        add_song:used to add a new song to the album's track list
    
    """
    def __init__(self, name, year, artist=None):
        self.name= name
        self.year= year
        if artist is None:
            self.artist = "various artist"
        else:
            self.artist = artist
        
        self.tracks=[]
        
    def add_song(self, song, position= None):
        """add a song to the track 

        Args:
            song (_type_): _description_
            position (_type_, optional): _description_. Defaults to None.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)
            
            
class Artist:
    """class to represent a artist
    
    attributes: 
    title (str): the title of the song 
    artist(artist): an artist object represnting the songs creator.
    duration(int): the duration of the song in seconds. may be zerp
    """
    def __init__(self, name):
        self.name = name 
        self.albums = []
    
    def add_album(self, album):
        """add new album to list 

        Args:
            album (album): album object to add in list
        """
        self.albums.append(album)
        
    def add_song(self, name, year, title):
        """add a new a song to the collection of albums 
        
        this method will add the song to an album in the collection 
        
        Args:
            name (str): _description_
            year (int): _description_
            title (_str): _description_
        """
        album_found= find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("foud album"+ name)
            
        album_found.add_song(title)
        
def find_object(field, object_list):
    """check 'object list' to see if an object  with a 'name' attritube equal to field exists, return it if so."""
    for item in object_list:
        if item.name == False:
            return item
    return None
     
 
def load_data():

    artist_list=[]
    
    with open("albums.txt","r") as album:
        for line in album:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
            
            new_artist= find_object(artist_field, artist_list)
            if new_artist is None:
               new_artist=Artist(artist_field)
               artist_list.append(new_artist)
            new_artist.add_song(album_field, year_field, song_field)

    return artist_list

def create_checkfile(artist_list):
    with open("checkfile.txt",'w')as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)
                        
            
                
                
            
if __name__ == '__main__':
    artists = load_data() 
    print("there are {} artist".format(len(artists)))
    
    create_checkfile(artists)

#help(Song.__init__)
#print(Song.__doc__)
#print(Song.__init__.__doc__)
#print(Album.__doc__)