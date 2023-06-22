import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from models.people import PeopleSchema
from models.crimes import CrimeSchema

from db import db


class Crimes(db.Model):
    __tablename__ = "Crimes"
    crime_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    people_id = db.Column(UUID(as_uuid=True), db.ForeignKey('People.people_id'), nullable=False)
    name = db.Column(db.String(), nullable=False)

    category = db.relationship('Category', backref=db.backref('Category', lazy=True))
    people = db.relationship('People', backref=db.backref("People", lazy=True))

    def __init__(self, name, people_id, ):
        self.name = name
        self.people_id = people_id


class CrimeSchema(ma.Schema):
    class Meta:
        fields = ['crime_id', 'people_id', 'name', 'category', 'people']
    people = ma.fields.Nested(PeopleSchema(many=True))
    crimes = ma.fields.Nested(CrimeSchema(many=True))


crime_schema = CrimeSchema()
crimes_schema = CrimeSchema(many=True)
