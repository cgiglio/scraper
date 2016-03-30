from application import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=False)
    description = db.Column(db.String(128), index=True, unique=False)
    byline = db.Column(db.String(128), index=True, unique=False)
    img = db.Column(db.String(128), index=True, unique=False)

    def __init__(self, title, description, byline, img):
        self.title = title
        self.description = description
        self.byline = byline
        self.img = img

    def __repr__(self):
        return '<Data %s %s %s' % self.description, self.byline, self.img
