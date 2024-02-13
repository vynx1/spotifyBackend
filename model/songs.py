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

# Function to create songs, store them in JSON format, and return the created songs
def initSongs():
    db.drop_all()
    db.create_all()
    
    Song1 = Song(name="FEIN", url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3", description="Travis Scott", uri="data:image/jpeg;base64,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", tokens="1", )
    Song2 = Song(name="Creepin", url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3", description="The Weeknd ", uri="https://i1.sndcdn.com/artworks-sWl8wb2Zk1xthx3m-39RYRQ-t500x500.jpg", tokens="2")
    


    db.session.add(Song1)
    db.session.add(Song2)

    db.session.commit()

if __name__ == "__main__":
    initSongs()
