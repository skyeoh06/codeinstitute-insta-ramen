import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import re
import math

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'ramen_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    top_three=mongo.db.ramens.find({'Stars': {'$gt': 3, '$lt':5}}).limit(3)
    return render_template('index.html', title="Home", top_three=top_three)
    
@app.route('/display_ramen/<ramen_id>', methods=['GET'])
def display_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    return render_template('display_ramen.html', title="Display Ramen", ramen=ramen)   
    
@app.route('/get_ramen')
def get_ramen():
    ramens=mongo.db.ramens.find()
    return render_template('ramen_collection.html', title="Ramen Collection", ramens=ramens)
    
@app.route('/ramen_asia')
def ramen_asia():
    ramens=mongo.db.ramens.find(
        {'$or':
            [{'Country': 'Taiwan'},{'Country': "Japan"}]
        }
        )
    return render_template('ramen_asia.html', title="Asian", ramens=ramens)
    
@app.route('/ramen_world')
def ramen_world():
    ramens=mongo.db.ramens.find(
        {'$or':
            [{'Country': 'Brunei'},{'Country': "Singapore"}]
        }
        )
    return render_template('ramen_world.html', title="Rest Of The World", ramens=ramens)    

@app.route('/search_ramen')
def search_ramen():
    orig_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    print(query)
    results=mongo.db.ramens.find({'Flavour': query})
    
    ramen = []
    for result in results:
        ramen.append(result)
    
    return render_template('ramen_search.html', title="Search Results", query=orig_query, ramen_search=ramen)
    
@app.route('/add_ramen')
def add_ramen():
    brands = mongo.db.brands.find()
    countries=mongo.db.countries.find()
    return render_template('add_ramen.html', title="Add a Ramen", countries=countries, brands=brands)
    
@app.route('/insert_ramen', methods=['POST'])
def insert_ramen():
    ramens = mongo.db.ramens
    ramens.insert_one(request.form.to_dict())
    return redirect(url_for('get_ramen'))    
    
@app.route('/edit_ramen/<ramen_id>', methods=['GET'])
def edit_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    countries = mongo.db.countries.find()
    return render_template('edit_ramen.html', title="Edit Ramen", ramen=ramen, countries=countries)

@app.route('/update_ramen/<ramen_id>', methods=["POST"])
def update_ramen(ramen_id):
    ramen = mongo.db.ramens
    ramen.update( {'_id': ObjectId(ramen_id)},
    {
        'Brand': request.form.get('Brand'),
        'Flavour':request.form.get('Flavour'),
        'Style': request.form.get('Style'),
        'Country':request.form.get('Country'),
        'Stars':request.form.get('Stars'),
        'Ratings':request.form.get('Ratings')
    })
    return redirect(url_for('get_ramen'))
    
@app.route('/delete_ramen/<ramen_id>')
def delete_ramen(ramen_id):
    mongo.db.ramens.remove({'_id': ObjectId(ramen_id)})
    return redirect(url_for('get_ramen'))
    
@app.route('/get_brands')
def get_brands():
    brands = mongo.db.brands.find()
    return render_template('brands.html', title="Ramen Brands", brands=brands)

@app.route('/add_brands')
def add_brands():
    brands = mongo.db.brands.find()
    add_a_brand = mongo.db.ramens.find()
    return render_template('add_brands.html', title="Add a Brand", add_a_brand=add_a_brand, brands=brands)
    
@app.route('/insert_brand', methods=['POST'])
def insert_brand():
    brand = mongo.db.brands
    brand.insert_one(request.form.to_dict())
    return redirect(url_for('get_ramen'))       
    
@app.errorhandler(404)
def error_404(not_found):
    return render_template('error404.html', title="Error 404", not_found=not_found)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    