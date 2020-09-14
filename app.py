import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'reunionPlanner'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
#app.config["MONGO_URI"] = os.environ.get(app.config["MONGO_URI"])

mongo = PyMongo(app)


@app.route('/')
@app.route('/add_schedule')
def add_schedule():
    return render_template("schedule.html", schedule=mongo.db.schedule.find())


if __name__ == '__main__':
    app.run(host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

#appbuilder = AppBuilder(app, db.session, base_template='mybase.html')
