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
    
    Song1 = Song(name="FEIN", url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3", description="Travis Scott", uri="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAOEg8PDw8VFREQEBAQERIWEBAVEBUSFRUWFhUVExgZHSggGBomGxcWITEtMSkrLi4yFx8zODMtNyk5LisBCgoKDg0NFRAQFi0eHR0tLSstLSstLS0rKy0rLSsrLSsrKysrLS0tLS0tLS0tLS0tNysrLS0tNy0rLS03LSsrK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABQECAwQGBwj/xAA9EAACAQMCAwcABgYLAQAAAAAAAQIDESEEEgUxQQYTIlFhcYEUMpGhsdEHQlLB4fAjM1NicpKToqPS8Rb/xAAXAQEBAQEAAAAAAAAAAAAAAAAAAQID/8QAHBEBAQEAAgMBAAAAAAAAAAAAAAEREkECITFR/9oADAMBAAIRAxEAPwDxMAFUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVSvZLm3ZF7p7W1Lna/zbCMZk3XSVsq/2eQFokg15CQFoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFUygAuDKBAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVCACKzjZlpnqRuk+qMAUAAAAAAAAAMkKMpZS/ADGDK9NNZ2P4V/wMbVsMCgAAAAAAAAAAAAAAAAAAAAAVKFQNjTtcmXa3SuFpLk8P0ZhguR02m06r0tr6pr13Iiz25QGTUUXTlKEucXb+JjKgAAABUAZ6M7dL/BgsZ47oxUk2pX6c7EI9I4FpOHVeGaqvWi6dehSqNNOynPb/AEcdvJ3k4rzuzl+P9n5wp0qtvF3cdyz4oRilGXvZP3si7ScRnV7nSSkpQ7yFVzynJQi593K31s9eaaN/iXEu9exq22e7m8pPc1jq0rfYUscMC+qkpSUfqqTUeXK+OXoWAAAAAAAAAAAAAAAAAAAAAAGSnL8Tp+EVFGEm20uj8mrM5Qk9LrbUpwfWxFlbvamjGXd14Lmts7dHzT9uZz5OcM4hslHfmPJp8rfkXcc4XHNfTx8HOUE77f7y8l6dCSrZ2gQAaZCpQqAN+G+cYJyjKz8Kx3lusMZ9TSir8vtMulltlGSeV+/mRYm+A8Ulp6t4Rjdpxyk0vJ/z5sa/WQlVqT8MlLcnGEpRcLW3SvZq25RtzvZkNGq7tx5v7rmWtxGoqf0dStDc5SWMvrZ9EF1oIAFZATXCuy2s1cO8o0rxvZNyUb9fDfma/EuA6vS27/Tzgmm72vGyy8xuibFyo0AFQAAAAAAAAAAAAAAAAAAGSFS2Dd4fxOVJ2eV09COBMJUrxTQ09qr0JJwk/HDrB/l+BGQhKV7Rbtzsm7e9i+lqHFSjzUlZ3/E67sVxdeLTVGkpfUVopXthZsPkaklrjAdJ2i4YoVd047FL1Vn5Z5GGnwilJJptXJpwqCuXKZ0vE+yboUoVW2nNJxT22km7eGzuYdJ2VqTtuur8sF2HGoOnUtnrmxl4dw+tqpqFGDk28v8AVXuzteH/AKPrLva82qaW54the50Wk1Ok0kFGhKNusm45+SWrPH9QGi7HaOn4dQqs5JLfKMrQjf2V7Y5+xx/H9PQpaicNM26UWrNu79cnQ9rO29XUXoUntpq6bjjd7nFt3yxN7Tys6dfS7bVKFONKhFLarKTXT2IriPaKvXu5zcpyxKb6L9mC6L8SFuZNPSdSUIJq85KKbdkm3a7fkXInKsYJ3ifZPV6dbnBVIWvupS3K3s0pfcQQ1MwABQAAAAAAAAAAAAAAAAAAF0IXwufRdW/JepsanSVtLKKqwlCTSlG/VeasYKU3FprmmmTnGuJvUU6EZZcG2va1iLIx6jilSvGmquVG23HV4uSfDNQozTWbNWTzf3IOdWz23VnZ3sr29PI63snChT3OrFy3R3brJ7VF3tG/JszXWJLj/aOpqJaanKyhQnLu3CFPDsld2xdWf2nSqnCnp41pJ7lduad3du+Y8mc5KjppRWolTleU25qKvTg7NZ5Pk/YwajjEG4rTTaaW1R5xa9SLEhr+2Uqse427cW3xzFr1T5HK8VVGnBwjHHPDxc3o6GUVOrXqpNu6jBJ3b6PyOW41Ve7n8FiX0iqjy7FoBtwDYjCm44lKM152cH7NZX3muAJzQ9o9RQWxzbiujd/Pk/lltSMNdUjs206073v4ac5c1e3Jvz8+fmQwUmmmuaaa9yY1yTH/AMtrf7D/AJaH/cGj9Jr/ALU/9wKnpqAAAAAAAAAAAAAAAAAAAZIO+LldNQlUlGEecnZeXu/QzQioRTazPr5Iixn4bpe9nGP2noejVKlRdOKV7re8fC/f8HnXDdS6dRSs84S/LzJ/Va5x2ucbXV0uTfq1czZrp42RJ9peMKiu7oW8SW5LlbyOcoVYwalKo6d8ycVd+y8mY5Vbu+28m8E1peFR7pzqxzJN/wDnoPh9Q2r7R1qr2zqOcU/C3bdbpe3UiK9Xc2zJxDaptRVkmaxqRztC9IokXFZWtFLFxQC0FWilgNr6dP8Abqf60waoAAAKAAAAAAAAAAAAAABJcG0Sqyc6ifdwcU7L603mML8ldKV/RASVDhMtPp6VaSkquq3bErqUKEbSU2rYUpJZ6RzbKvr1tepeJpZjKFo01ttb+szlSvfpbw39/WeyHYqOt02qWsqyjFwcd8G4OjUg01s6WSTune/3nluv0TpPUU414Ve4moKpGm1CpCU8S2ON7pp3Tx4Xl4bitejPvE5y+s1FRjFzVJSe5xc425O0Vz6562rpZ0ZKcqjbqJXbzZrz3eJfGOhv0uDyTdnGnPbUdpQbpPbeLyr7Ve7WbYXXBGaui9qTpwp1FeLUZcrNpxXk8Pq+fqE1M8C1+muspVMtKptjFeu7r7LLNLjXaKUnKEJXXK6Vo/Bz1SLxdfNuf5lgxedwbvllyRRIuKyqUFygUBm0ekqV5d3Sg5Tcak9qtfbThKc3nyjGT+DZpcE1M9u2hJ7p6emsxS36iHeUVl43RyBHg3J8K1EYqbpNRlShXjmN5Upz7uMoq95XnjGTFrNDVoNKrBxbdSKvbnTk4TWPKSa+ANcAAAAAAAAAAAAAAAAFTY0lGMpf0ktsVl2+s/ReQGukd7wDT0aGiTrxU4ajc3DdOF2lZuTi08bkl7S53OOr14KVqa8CthopGvKKcdz2yd4vyd0/z+0hK9o7P9sZ1dPrqDlFWh3jqwioz22alCUXe7tFPcr4ksWV35BX19SN0qkbQbsn4pNtO+Grc2+fXLNTT6xwVRXxNWasld2lFXt6SkYKNRwanG14vF1fz+AanqPFa219/HFvC793N38Lh4Pq3XWyxjqRGvk3Pfs2KUYtLo/CrtNc/wCJjU8rx2u919t9rbzueL4zi6z6ss71rck/C8Wa6Lli7s/nBUU3Sd+efdiK5/zn+blrK2tz8k182/dcC4FAAAAV6B+ibhtPUPVuWnVaUZ6CC8Lk40alfbqeXR0d6fuek0ez0bprSO0fptTc6U09+mnSp6S3LMVOSg/Knh9X8/8ADNWqFWFWVKFVRU13c0nB7oSirpp8r3+ESVPtBTUnJ6DTO+1W7uG3wt2xt8mk/OxEe1cQ7O0k0qWibcIcWhGX0aolFae09JGDcfDFTfh/aabW61zmf0o8DhR4dHUSoqM3U0EovY1KM61KpPU5fWU0m/VHnWm49Tp0o0voGnlJQ2upKnF1Hmnm+3n4H/nkaXF+Ix1Dg46elRUE1anCMd2Iq8rJXePvYGgACgAAoAAAAAAAAAANvhf9YvZmDU817AAYzL+p8oqAjCEAAAABl9X9X/BH8AALQAAAAVQAAAAEAAB//9k=", tokens="1", )
    Song2 = Song(name="Creepin", url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3", description="The Weeknd ", uri="https://i1.sndcdn.com/artworks-sWl8wb2Zk1xthx3m-39RYRQ-t500x500.jpg", tokens="2")
    Song3 = Song(name="Good Days", url="", description=" SZA", uri="https://upload.wikimedia.org/wikipedia/en/7/7c/SZA_-_Good_Days.png", tokens="3")
    Song4 = Song(name="Role Model", url="", description=" Brent Fiaiyaz", uri="https://i1.sndcdn.com/artworks-O2SRR9SCgyRq4u4v-eAojjA-t500x500.jpg", tokens="4")
    Song5 = Song(name="Right my Wrongs", url="", description=" Bryson Tiller", uri="https://static.wikia.nocookie.net/justin-bieber/images/3/33/T_R_A_P_S_O_U_L.jpg/revision/latest?cb=20200928002537", tokens="5")
    Song6 = Song(name="Roar", url="", description=" Katy Perry", uri="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_Y92S1N976xSO57PbyPinyoJ8IVnqGPFhLQ&usqp=CAU", tokens="6")
    Song7 = Song(name="Shake it Off", url="", description=" Taylor Swift", uri="https://pyxis.nymag.com/v1/imgs/2d9/6f5/3f8dbd63613637b7843e4653ff548503b9-tay--.w710.jpg", tokens="7")
    Song8 = Song(name="Often", url="", description=" The Weeknd", uri="https://cdns-images.dzcdn.net/images/cover/eea9f7fc913300e40307a0ff70dc73cf/350x350.jpg", tokens="8")
    Song9 = Song(name="Thank God", url="", description=" Travis Scott", uri="data:image/jpeg;base64,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", tokens="9")
    Song10 = Song(name="God did ", url="", description=" DJ Khalid", uri="https://upload.wikimedia.org/wikipedia/en/0/0a/DJ_Khaled_-_God_Did.png", tokens="10")
    Song11 = Song(name="Badtameez Dil", url="", description=" Yeh Jawaani Hai Deewani", uri="https://m.media-amazon.com/images/M/MV5BODA4MjM2ODk4OF5BMl5BanBnXkFtZTcwNDgzODk1OQ@@._V1_FMjpg_UX1000_.jpg", tokens="11")
    Song12 = Song(name="Same Old Love", url="", description=" Selena Gomez", uri="https://upload.wikimedia.org/wikipedia/en/b/b3/Same_Old_Love_by_Selena_Gomez.png", tokens="12")
    Song13 = Song(name="Waka Waka ", url="", description=" Shakira", uri="https://photos.prnewswire.com/prnfull/20100901/NY58538-a", tokens="13")
    Song14 = Song(name="Swim", url="", description=" Chase Atlantic ", uri="https://i.ytimg.com/vi/ykP640XEjSQ/maxresdefault.jpg", tokens="14")
    Song15 = Song(name="Fireside", url="", description=" Arctic Monkeys", uri="https://i.ytimg.com/vi/PG8yTUeptFU/maxresdefault.jpg", tokens="15")
    Song16 = Song(name="Daddy Issues", url="", description=" The Neighborhood", uri="https://i.scdn.co/image/ab67616d0000b2733066581d697fbdee4303d685", tokens="16")
    Song17 = Song(name="Art Deco", url="", description="Lana Del Rey ", uri="https://static.wikia.nocookie.net/lanadelrey/images/1/19/Honeymoon.jpg/revision/latest?cb=20170706082252", tokens="17")
    Song18 = Song(name="The Color Violet", url="", description=" Tory Lanez ", uri="https://i1.sndcdn.com/artworks-XTdw6XGAR3WX-0-t500x500.jpg", tokens="18")


    db.session.add(Song1)
    db.session.add(Song2)
    db.session.add(Song3)
    db.session.add(Song4)
    db.session.add(Song5)
    db.session.add(Song6)
    db.session.add(Song7)
    db.session.add(Song8)
    db.session.add(Song9)
    db.session.add(Song10)
    db.session.add(Song11)
    db.session.add(Song12)
    db.session.add(Song13)
    db.session.add(Song14)
    db.session.add(Song15)
    db.session.add(Song16)
    db.session.add(Song17)
    db.session.add(Song18)

    db.session.commit()

if __name__ == "__main__":
    initSongs()
