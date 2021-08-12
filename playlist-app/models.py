"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = "playlist"

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)

    name = db.Column(db.String(50))
    
    description = db.Column(db.String(5000))
    
    playlistsong = db.relationship('PlaylistSong',backref="playlist")


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = "songs"

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)

    title = db.Column(db.String(50))
    
    artist = db.Column(db.String(500))

    playlistsong = db.relationship('PlaylistSong',backref="songs")

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = "playlistsong"

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)

    playlist_id = db.Column(db.Integer,db.ForeignKey("playlist.id",ondelete="cascade"))

    song_id = db.Column(db.Integer,db.ForeignKey("songs.id",ondelete="cascade"))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
