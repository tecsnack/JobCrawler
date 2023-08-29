python
from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/crawl', methods=['GET'])
def crawl():
    keywords = request.args.get('keywords').split(',')
    # Hier den Code für den Crawler einfügen, um die Jobangebote zu extrahieren und in eine CSV-Datei zu speichern
    
    # Öffne die CSV-Datei und lies den Inhalt ein
    with open('job_listings.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()