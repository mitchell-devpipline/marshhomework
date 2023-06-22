from flask import Flask, request, jsonify

from db import *
from models.crimes import Crimes, crime_schema, crimes_schema


def add_crime():
    req_data = request.form if request.form else request.json

    fields = ['crime_id', 'people_id', 'name', 'cat_id']
    req_fields = ['crime_id', 'people_id', 'name', 'cat_id']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_crime = Crimes(
        values['crime_id'],
        values['people_id'],
        values['name'],
        values['cat_id'])

    db.session.add(new_crime)
    db.session.commit()

    return jsonify('Crime Added'), 200
