import os
import random
from flask import Flask,render_template, url_for, json,jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["60 per hour"]
)


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



"""[Method to build the payload]
    
    Arguments:
        data {[json]}
    
    Returns:
        [payload] -- [json object]
"""
    
def payloadBuilder(data):
    
    # Getting the black and white cards
    decks=data['order']
    blackCards=data['blackCards']
    whiteCards=data['whiteCards']
    
    # Selecting a deck randomly
    deck=random.choice(decks)
    selectedDeck=data[deck]
    
    # Selecting the object for the selected deck name
    selectedDeckName=selectedDeck['name']
    selectedDeckBlack=selectedDeck['black']
    selectedDeckWhite=selectedDeck['white']
    selectedDeckIcon=selectedDeck['icon']
    selectedDeckBlackIndex=random.choice(selectedDeckBlack)
    
    # Picking white and black card accoring to the pick and the selected deck
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
        'blackCard': blackCard['text'],
        'whiteCard': whiteCard, 
        'icon': selectedDeckIcon
    }
    ]
    
    return payload
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0')
