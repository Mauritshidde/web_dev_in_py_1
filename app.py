from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3, json, collections, sys, os
from forms import AcountmakenForm, AddproductForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd1ccabe4c9d3d5813ba8881bd1082fef'
y = {}

conn = sqlite3.connect('gebruikers.db')
c = conn.cursor()

#c.execute("""CREATE TABLE gebruikers (
            #product text,
            #product_soort text,
            #product_prijs int
            #)""")
def maak_API(y):
    conn = sqlite3.connect('producten.db')
    c = conn.cursor()
    c.execute("SELECT product, product_soort, product_prijs FROM producten")
    rows = c.fetchall()
    for row in rows:
        x = {
            row[0]: {
                'product_soort': row[1],
                'product_prijs': row[2]}
            }
        y.update(x)

        with open("producten.json", "w") as write_file:
            json.dump(y, write_file)

def acount_toevoegen(username, password):
    conn = sqlite3.connect('gebruikers.db')
    c = conn.cursor()
    bestaatal = c.execute("SELECT * FROM gebruikers WHERE username = :first",
                {'first': username}).fetchall()
    if bestaatal:
        pass
    else:
        c.execute("INSERT INTO gebruikers VALUES('{}', '{}')".format(username, password))
    conn.commit()

def product_toevoegen(product, product_soort, product_prijs):
    conn = sqlite3.connect('producten.db')
    c = conn.cursor()
    bestaatal = c.execute("SELECT * FROM producten WHERE product = :first",
                {'first': product}).fetchall()
    if bestaatal:
        pass
    else:
        c.execute("INSERT INTO producten Values('{}', '{}', '{}')".format(product, product_soort, product_prijs))
    conn.commit()

@app.route('/makeacount', methods=['GET', 'POST'])
def acount_aanmaken():
    form=AcountmakenForm()
    if form.submit():
        username = form.username.data
        password = form.password.data
        acount_toevoegen(username, password)
    return render_template('acount_aanmaken.html', form=form)

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    form=AddproductForm()
    if form.submit():
        product = form.product.data
        product_soort = form.product_soort.data
        product_prijs = form.product_prijs.data
        print(product, product_soort, product_prijs)
        product_toevoegen(product, product_soort, product_prijs)
    return render_template('addproduct.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def shop():
    maak_API(y)
    productenAPI = y
    print(productenAPI)
    return render_template('webshop.html')

app.run(host='localhost', port=8080, debug=True)
