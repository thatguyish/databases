from models import db,Song,Playlist, PlaylistSong
from app import app

db.drop_all()
db.create_all()

song1 = Song(title="mysongtitle",artist="john")

playlist1 = Playlist(name="bestplaylist", description="best playlist ever bruh")

playlistsong1 = PlaylistSong(song_id=1, playlist_id=1)


db.session.add_all([song1,playlist1])
db.session.commit()
db.session.add(playlistsong1)
db.session.commit()