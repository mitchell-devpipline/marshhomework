import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class People(db.Model):
    __tablename__ = "People"

    person_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, first_name, last_name, email, active):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active


class PeopleSchema(ma.Schema):
    class Meta:
        fields = ['person_id', 'first_name', 'last_name', 'email', 'active']


person_schema = PeopleSchema()
people_schema = PeopleSchema(many=True)
