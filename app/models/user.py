from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))

    def __repr__(self):
        return f'<User "{self.name}">'

    @property
    def serialized(self):
        return {
            "id": self.id,
            "name": self.name,
        }
