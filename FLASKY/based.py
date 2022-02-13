from flask import *
import  sqlite3
import os
 
app = Flask(__name__)

def tops():
    connection = sqlite3.connect('Products/produits.db')
    cur = connection.cursor()
    request_tops = """
    SELECT produit, prix FROM PRODUCTS WHERE categorie  = 'tops' 
    """
    response_tops = cur.execute(request_tops)
    table_tops = response_tops.fetchall()
    connection.close()
    return table_tops

def bottoms():
    connection = sqlite3.connect('Products/produits.db')
    cur = connection.cursor()
    request_bottoms = """
    SELECT produit, prix FROM PRODUCTS WHERE categorie  = 'bottoms' 
    """
    response_bottoms = cur.execute(request_bottoms)
    table_bottoms = response_bottoms.fetchall()
    connection.close()
    return table_bottoms

def gift_cards():
    connection = sqlite3.connect('Products/produits.db')
    cur = connection.cursor()
    request_gift_cards = """
    SELECT produit, prix FROM PRODUCTS WHERE categorie  = 'gift-cards' 
    """
    response_gift_cards = cur.execute(request_gift_cards)
    table_gift_cards = response_gift_cards.fetchall()
    connection.close()
    return table_gift_cards

def accessories():
    connection = sqlite3.connect('Products/produits.db')
    cur = connection.cursor()
    request_accessories = """
    SELECT produit, prix FROM PRODUCTS WHERE categorie  = 'accessories' 
    """
    response_accessories = cur.execute(request_accessories)
    table_accessories = response_accessories.fetchall()
    connection.close()
    return table_accessories

def jackets():
    connection = sqlite3.connect('Products/produits.db')
    cur = connection.cursor()
    request_jackets = """
    SELECT produit, prix FROM PRODUCTS WHERE categorie  = 'jackets' 
    """
    response_jackets = cur.execute(request_jackets)
    table_jackets = response_jackets.fetchall()
    connection.close()
    return table_jackets

@app.route("/")
def index():
    return render_template('my_index.html')

@app.route("/shop")
def unboxing():
    return render_template("unbox.html")

@app.route("/register")
def registration():
    return render_template("registration.html")

@app.route("/shop/tops")
def tops_page():
    return render_template("tops.html", table_tops=tops())

@app.route("/shop/bottoms")
def bottoms_page():
    return render_template("bottoms.html", table_bottoms=bottoms())

@app.route("/shop/gift-cards")
def cards_page():
    return render_template("gift_cards.html", table_gift_cards=gift_cards())

@app.route("/shop/accessories")
def accessories_page():
    return render_template("accessories.html", table_accessories=accessories())

@app.route("/shop/jackets")
def jackets_page():
    return render_template("jackets.html", table_jackets=jackets())

if __name__ == "__main__":
    app.run(debug=True)