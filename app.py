from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from mission_to_mars import scrape


app = Flask(__name__)
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_db')

@app.route('/')
def home():
    mars_data = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars_data)

@app.route('/scrape')
def scrape_mars():
    mars = scrape()
    mongo.db.mars.update({},mars, upsert=True)
    return redirect('/', code=302)

    






if __name__ == '__main__':
    app.run(debug=True)
