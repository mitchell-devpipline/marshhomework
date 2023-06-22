from flask import Flask, request, jsonify

from db import *
from models.sentance import Sentance, sentance_schema, sentances_schema


def add_sentance():
    req_data = request.form if request.form else request.json

    fields = ['sentance_id', 'people_id', 'crime_id', 'prison_sentance', 'death_penalty', 'bail_amount']
    req_fields = ['sentance_id', 'people_id', 'crime_id', 'prison_sentance']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_sentence = Sentance(
        values['sentance_id'],
        values['people_id'],
        values['crime_id'],
        values['prison_sentance'],
        values['death_penalty'],
        values['bail_amount'])

    db.session.add(new_sentence)
    db.session.commit()

    return jsonify('Sentance Created'), 200
