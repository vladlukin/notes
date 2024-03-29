# app.py
from flask import Flask, request, jsonify
from notes_dao import add_note

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

notes = {"id":1, "text": "initial empty body"}
   

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/notes")
def get_notes():
    return jsonify(notes)

@app.post("/notes")
def edit_note():
    note_id = 1
    if request.is_json:
        new_text = request.get_json()
        notes["text"] = new_text
        return notes, 201
    return {"error": "Request must be JSON"}, 415

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

@app.get("/add-note-test/<body>")
def add_note_test(body):
    account_id = 1
    add_note(account_id, body)
    return {"status": "success"}, 200

@app.post("/add-note")
def add_note_test(body):
    account_id = 1
    add_note(account_id, body)
    return {"status": "success"}, 200


app.run(host='::', port=5000, debug=True)
