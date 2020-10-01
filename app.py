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


@app.route('/')  #code from task manager mini-project to show list of people
@app.route('/get_people')
def get_people():
    return render_template("people.html", 
                           people=mongo.db.people.find())


@app.route('/add_people')  #code from task manager mini-project to add people
def add_task():
    return render_template('addpeople.html',
                           people=mongo.db.people.find())


@app.route('/insert_people', methods=['POST'])  #code from task manager mini-project to add people
def insert_people():
    people = mongo.db.people
    people.insert_one(request.form.to_dict())
    return redirect(url_for('get_people'))


@app.route('/edit_people/<person_id>')
def edit_person(person_id):
    the_person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    all_people = mongo.db.people.find()
    return render_template('editpeople.html', person=the_person)


@app.route('/update_task/<task_id>', methods=["POST"])
def update_person(person_id):
    people = mongo.db.people
    people.update( {'_id': ObjectId(person_id)},
    {
        'name':request.form.get('name'),
        'time_zone':request.form.get('time_zone'),
        'is_coming': request.form.get('is_coming'),
        'accommodations': request.form.get('accommodations'),
        'dietary_restrictions':request.form.get('dietary_restrictions')
    })
    return redirect(url_for('get_people'))


@app.route('/delete_person/<person_id>')  #code from task manager mini project to delete people
def delete_person(person_id):
    mongo.db.person.remove({'_id': ObjectId(person_id)})
    return redirect(url_for('get_people'))


@app.route('/get_schedule')   #code from task manager mini-project to show schedule
def get_schedule():
    return render_template('schedule.html',
                           schedule=mongo.db.schedule.find())


@app.route('/add_item')
def add_item():
    return render_template('additem.html',
                           schedule=mongo.db.schedule.find())


@app.route('/insert_item', methods=['POST'])
def insert_item():
    schedule = mongo.db.schedule
    schedule.insert_one(request.form.to_dict())
    return redirect(url_for('get_schedule'))


@app.route('/edit_item/<item_id>')
def edit_item(item_id):
    the_item = mongo.db.schedule.find_one({"_id": ObjectId(item_id)})
    all_schedule = mongo.db.all_schedule.find()
    return render_template('editschedule.html', item=the_item,
                           schedule=all_schedule)


@app.route('/update_item/<item_id>', methods=["POST"])
def update_item(item_id):
    schedule = mongo.db.schedule
    schedule.update( {'_id': ObjectId(item_id)},
    {
        'day':request.form.get('day'),
        'morning':request.form.get('morning'),
        'afternoon': request.form.get('afternoon'),
        'dinner': request.form.get('dinner'),
        'evening':request.form.get('evening')
    })
    return redirect(url_for('get_schedule'))


@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    mongo.db.schedule.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('get_schedule'))


if __name__ == '__main__':
    app.run(host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

#appbuilder = AppBuilder(app, db.session, base_template='mybase.html')
