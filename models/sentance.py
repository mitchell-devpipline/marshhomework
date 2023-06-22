import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from models.people import PeopleSchema
from models.crimes import CrimeSchema
from db import db


class Sentance(db.Model):
    __tablename__ = "Sentance"
    sentance_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    people_id = db.Column(UUID(as_uuid=True), db.ForeignKey('People.people_id'), nullable=False)
    crime_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Crimes.crime_id'), nullable=False)
    prison_sentance = db.Column(db.Integer(), nullable=False)
    death_penalty = db.Column(db.Boolean(), default=True)
    bail_amount = db.Column(db.Integer())

    people = db.relationship('People', backref=db.backref("Sentance", lazy=True))
    crimes = db.relationship('Crimes', backref=db.backref("Crimes", lazy=True))

    def __init__(self, people_id, crime_id, prison_sentance, death_penalty, bail_amount):
        self.people_id = people_id
        self.crime_id = crime_id
        self.prison_sentance = prison_sentance
        self.death_penalty = death_penalty
        self.bail_amount = bail_amount


class SentanceSchema(ma.Schema):
    class Meta:
        fields = ['sentance_id', 'people_id', 'crime_id', 'prison_sentance', 'death_penalty', 'bail_amount', 'people', 'crimes']
    people = ma.fields.Nested(PeopleSchema(many=True))
    crimes = ma.fields.Nested(CrimeSchema(many=True))


sentance_schema = SentanceSchema()
sentances_schema = SentanceSchema(many=True)
