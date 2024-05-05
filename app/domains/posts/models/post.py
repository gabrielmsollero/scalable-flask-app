# Reused from DigitalOcean's guide
# Original version available at https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author_id = db.Column(db.Integer)
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post "{self.title}">'

    @property
    def serialized(self):
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id,
            "content": self.content,
        }
