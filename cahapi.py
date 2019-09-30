import os
import random
from flask import Flask, render_template, url_for, json, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin
import re

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["600 per hour"]
)


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "", "cards.json")
data = json.load(open(json_url))


"""[Default route for the main endpoint returning json ]

Returns:
    [json] 
"""
@app.route("/")
@cross_origin()
def index():
    payload = payloadBuilder(data)
    return jsonify(payload)


"""[Method to build the payload]
    
    Arguments:
        data {[json]}
    
    Returns:
        [payload] -- [json object]
"""


def payloadBuilder(data):

    # Getting the black and white cards
    decks = data['order']
    blackCards = data['blackCards']
    whiteCards = data['whiteCards']

    # Selecting a deck randomly
    deck = random.choice(decks)
    selectedDeck = data[deck]

    # Selecting the object for the selected deck name
    selectedDeckName = selectedDeck['name']
    selectedDeckBlack = selectedDeck['black']
    selectedDeckWhite = selectedDeck['white']
    selectedDeckBlackIndex = random.choice(selectedDeckBlack)

    # Picking white and black card accoring to the pick and the selected deck
    blackCard = blackCards[selectedDeckBlackIndex]
    blackCardPick = blackCard['pick']
    whiteCard = []
    # while blackCardPick > 0:
    #     selectedDeckWhiteIndex = random.choice(selectedDeckWhite)
    #     whiteCard.append(whiteCards[selectedDeckWhiteIndex])
    #     blackCardPick -= 1

    if blackCardPick == 1:
        selectedDeckWhiteIndex = random.choice(selectedDeckWhite)
        whiteCard.append(whiteCards[selectedDeckWhiteIndex])
        payload = [
            {
                'name': selectedDeckName,
                'blackCard': cleanhtml(blackCard['text']),
                'whiteCard': whiteCard,
                'index': selectedDeckBlackIndex,
                'deck':deck,
                'stuff':blackCard
            }
        ]
        return payload

        # blackCardPick -= 1


"""[For fetching white cards ]

Returns:
    [json] 
"""
@app.route("/fetchWhite", methods=['POST'])
@cross_origin()
def fetchWhite():
    postData = request.get_json()
    deck = postData['deck']
    cards = postData['cards']
    selectedDeck = data[deck]
    whiteCardDeck = selectedDeck['white']
    whiteCards = []
    while cards > 0:
        whiteCard = random.choice(whiteCardDeck)
        whiteCards.append(whiteCard)
        cards -= 1

    postData['white'] = whiteCards
    return jsonify(postData)


"""[Removing HTML tags]

Returns:
    [String] -- [Cleaned text]
"""


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
