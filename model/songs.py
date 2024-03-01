from __init__ import app, db

class Song(db.Model):  
    __tablename__ = 'songs'  

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _url = db.Column(db.String(255), unique = False, nullable=False)
    _description = db.Column(db.String(255), unique=True, nullable=False)
    _uri = db.Column(db.String(255), unique=False, nullable=False)
    _tokens = db.Column(db.Integer)
    
    def __init__(self, name, url, description, uri, tokens):
        self._name = name
        self._description = description
        self._url = url  # Corrected assignment to _url
        self._uri = uri
        self._tokens = tokens

    def to_dict(self):
        return {"id": self.id, "_name": self._name, "url": self._url, "_description": self._description, "_uri": self._uri, "_tokens": self._tokens}
    
    print("WOOHOO 3")

# Function to create songs, store them in JSON format, and return the created songs
def initSongs():
    with app.app_context():

        db.create_all()

        

        songs_data = [
    {'name':'Creepin', 'url':'/audios/CREEP.mp3', 'description':'The Weeknd_ ', 'uri':'https://i1.sndcdn.com/artworks-sWl8wb2Zk1xthx3m-39RYRQ-t500x500.jpg', 'tokens':'1'},
    ]
        
        print("WOOHOO 2")
        
        # iterate
        for song_data in songs_data:
            existing_song = Song.query.filter_by(_name=song_data['name']).first()
            # If user exists, print a message and update user data
            if existing_song:
                print(f"User with _uid '{song_data['name']}' already exists. Updating user data.")
                # If user does not exist, create a new user and add to the database
            else:
                new_song = Song(
                    name=song_data['name'],
                    url=song_data['url'],
                    description=song_data['description'],
                    uri=song_data['uri'],
                    tokens=song_data['tokens']   
                )
                db.session.add(new_song)
        db.session.commit()
        
        
if __name__ == "__main__":
    initSongs()
