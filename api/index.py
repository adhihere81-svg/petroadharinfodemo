from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FILE = os.path.join(BASE_DIR, "data.csv")

def search_number(number):
    results = []

    with open(CSV_FILE, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["phoneNumber"] == number:
                results.append(row)

    return results

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "API Running"
    })

@app.route("/search")
def search():
    try:
        number = request.args.get("number")

        if not number:
            return jsonify({
                "success": False,
                "message": "Number parameter required"
            })

        results = search_number(number)

        if results:
            return jsonify({
                "success": True,
                "total": len(results),
                "results": results
            })

        return jsonify({
            "success": False,
            "message": "No data found"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

app = app
