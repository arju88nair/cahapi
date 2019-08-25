import os
import random
from flask import Flask,render_template, url_for, json,jsonify
app = Flask(__name__)


"""[Default route for the main endpoint returning json ]

Returns:
    [json] 
"""
@app.route("/")
def index():
    
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "", "cards.json")
    data = json.load(open(json_url))
    payload=payloadBuilder(data)
    return jsonify(payload)




    
def payloadBuilder(data):
"""[Method to buold the payload]
    
    Arguments:
        data {[json]}
    
    Returns:
        [payload] -- [json object]
    """
    
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
    
    blackCard=blackCards[selectedDeckBlackIndex]
    blackCardPick=blackCard['pick']        
    whiteCard=[]
    while blackCardPick > 0:
        selectedDeckWhiteIndex=random.choice(selectedDeckWhite)
        whiteCard.append(whiteCards[selectedDeckWhiteIndex])
        blackCardPick-=1
    
    
    
    payload= [
    {
        'name': selectedDeckName,
        'blackCard': blackCard,
        'whiteCard': whiteCard, 
        'done': blackCardPick
    }
    ]
    return payload
    
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0')
