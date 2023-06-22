import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
# from models.crimes import CrimeSchema

from db import db


class CrimeCategories(db.Model):
    __tablename__ = "CrimeCategories"
    cat_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    severity = db.Column(db.Integer())
    convicted = db.Column(db.Boolean())

    def __init__(self, cat_id, name, severity, convicted):
        self.cat_id = cat_id
        self.name = name
        self.severity = severity
        self.convicted = convicted


class CrimeCatSchema(ma.Schema):
    class Meta:
        fields = ['cat_id', 'name', 'severity', 'convicted',]


crimecat_schema = CrimeCatSchema()
crimecats_schema = CrimeCatSchema(many=True)
