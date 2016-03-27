from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)
    parent = db.Column(db.String(64))
    lunch = db.Column(db.Boolean, default=False)
    chaperone = db.Column(db.Boolean, default=False)
    chapName= db.Column(db.String(64), default = '')
    notes = db.Column(db.Text, default = '')
    # email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

class Chap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    parent = db.Column(db.String(64))
    kids = db.Column(db.Text, default = '')
    # email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
