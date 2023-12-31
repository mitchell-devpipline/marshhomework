import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from models.people import PeopleSchema
from models.crime_categories import CrimeCatSchema

from db import db


class Crimes(db.Model):
    __tablename__ = "Crimes"
    crime_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    person_id = db.Column(UUID(as_uuid=True), db.ForeignKey('People.person_id'), nullable=False)
    cat_id = db.Column(UUID(as_uuid=True), db.ForeignKey('CrimeCategories.cat_id'), nullable=False)
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
    category = ma.fields.Nested(CrimeCatSchema(many=True))


crime_schema = CrimeSchema()
crimes_schema = CrimeSchema(many=True)
