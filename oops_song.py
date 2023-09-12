
class Song:
    """class to represent a song 
    
    attributes: 
    title (str): the title of the song 
    artist(artist): an artist object represnting the songs creator.
    duration(int): the duration of the song in seconds. may be zerp
    """
    def __init__(self, title, artist, duration = 0):
      
        self.title = title
        self.artist = artist
        self.duration = duration
        
class Album:
    """class to represent songs albums 
    
    attributes: 
    title (str): the title of the song 
    artist(artist): an artist object represnting the songs creator.
    duration(int): the duration of the song in seconds. may be zerp
    """
    def __init__(self, name, year, artist= None):
        self.name= name
        self.year= year
        if artist is None:
            self.artist = Artist("various artist")
        else:
            self.artist = artist
        
        self.tracks=[]
        
    def add_song(self, song, position= None):
        """add a song to the track 

        Args:
            song (_type_): _description_
            position (_type_, optional): _description_. Defaults to None.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song )
            
            
class Artist:
    """class to represent a artist
    
    attributes: 
    title (str): the title of the song 
    artist(artist): an artist object represnting the songs creator.
    duration(int): the duration of the song in seconds. may be zerp
    """
    def __init__(self, name):
        self.name = name 
        self.album = []
    
    def add_album(self, album):
        """add new album to list 

        Args:
            album (album): album object to add in list
        """
        self.album.append(album)
        
def find_object(field, object_list):
    """check 'object list' to see if an object  with a 'name' attritube equal to field exists, return it if so."""
    for item in object_list:
        if item.name == False:
            return item
    return None
     
 
def load_data():
    new_artist = None
    new_album = None
    artist_list=[]
    
    with open("albums.txt","r") as album:
        for line in album:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
            
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                #we 've just read the details for new artist
                #retrieve the artist object if there is one,
                #otherwise create a new object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None
            
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                #we 've read a new album 
                #retrieve the album object if there is any 
                #otherwise create a new album object and store it in artist collection
                new_album = find_object(album_field, new_artist.album)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)
                           
            #create new song oject n add it to current songs collection 
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)
                        
    return artist_list

def create_checkfile(artist_list):
    with open("checkfile.txt",'w')as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.album:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),file= checkfile)
                        
            
                
                
            
if __name__ == '__main__':
    artists = load_data() 
    print("there are {} artist".format(len(artists)))
    
    create_checkfile(artists)

#help(Song.__init__)
#print(Song.__doc__)
#print(Song.__init__.__doc__)
#print(Album.__doc__)