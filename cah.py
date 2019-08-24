import os
import random
from flask import Flask,render_template, url_for, json,jsonify
app = Flask(__name__)


@app.route("/")
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "", "cards.json")
    data = json.load(open(json_url))
    decks=data['order']
    blackCards=data['blackCards']
    whiteCards=data['whiteCards']
    
    deck=random.choice(decks)
    selectedDeck=data[deck]
    
    selectedDeckName=selectedDeck['name']
    selectedDeckBlack=selectedDeck['black']
    selectedDeckWhite=selectedDeck['white']
    selectedDeckIcon=selectedDeck['icon']
    selectedDeckBlackIndex=random.choice(selectedDeckBlack)
    selectedDeckWhiteIndex=random.choice(selectedDeckWhite)
    
    blackCard=blackCards[selectedDeckBlackIndex]['text']
    whiteCard=whiteCards[selectedDeckWhiteIndex]
    
    
    
    payload= [
    {
        'name': selectedDeckName,
        'blackCard': blackCard,
        'whiteCard': whiteCard, 
        'done': True
    }
]
    
    return jsonify(payload)
    

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0')
