import os
from flask import Flask
#from flask_pymongo import PyMongo
#from bson.objectid import ObjectId


app = Flask(__name__)


#mongo = PyMongo(app)


#appbuilder = AppBuilder(app, db.session, base_template='mybase.html')


@app.route('/')
def hello():
    return "Hello World...again"


if __name__ == '__main__':
    app.run(host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)