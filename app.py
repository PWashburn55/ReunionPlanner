import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

#if os.path.exists("env.py"):
#    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'reunionPlanner'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
# app.config["MONGO_URI"] = os.environ.get(app.config["MONGO_URI"])

mongo = PyMongo(app)


@app.route('/')  # code from task manager mini-project
@app.route('/get_home')
def get_home():
    return render_template("index.html")


@app.route('/')  # from task manager mini-project to show list of people
@app.route('/get_people')
def get_people():
    the_person = mongo.db.people.find()
    return render_template('people.html', people=the_person, person=the_person)


@app.route('/add_person')  # from task manager mini-project to add people
def add_person():
    the_person = mongo.db.people.find()
    return render_template('addpeople.html',
                           people=mongo.db.people.find(), person=the_person)


@app.route('/insert_person', methods=['POST'])  # from task mgr to add people
def insert_person():
    people = mongo.db.people
    people.insert_one(request.form.to_dict())
    return redirect(url_for('get_people'))


@app.route('/edit_person/<person_id>')
def edit_person(person_id):
    the_person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    return render_template('editpeople.html', person=the_person)


@app.route('/update_person/<person_id>', methods=["POST"])
def update_person(person_id):
    people = mongo.db.people
    people.update({'_id': ObjectId(person_id)},
                  {
                    'name': request.form.get('name'),
                    'time_zone': request.form.get('time_zone'),
                    'is_coming': request.form.get('is_coming'),
                    'accommodations': request.form.get('accommodations'),
                    'diet': request.form.get('diet')
                  })
    return redirect(url_for('get_people'))


#@app.route('/delete_person/<person_id>')  # from task manager to delete people
#def delete_person(person_id):
   # mongo.db.person.remove({'_id': ObjectId(person_id)})
    # return redirect(url_for('get_people'))


@app.route('/get_schedule')   # from task manager mini-project to show schedule
def get_schedule():
    the_item = mongo.db.schedule.find()
    return render_template('schedule.html',
                           schedule=mongo.db.schedule.find(), item=the_item)


@app.route('/add_item')
def add_item():
    the_item = mongo.db.schedule.find()
    return render_template('addschedule.html',
                           schedule=mongo.db.schedule.find(), item=the_item)


@app.route('/insert_item', methods=['POST'])
def insert_item():
    schedule = mongo.db.schedule
    schedule.insert_one(request.form.to_dict())
    return redirect(url_for('get_schedule'))


@app.route('/edit_item/<item_id>')
def edit_item(item_id):
    the_item = mongo.db.schedule.find_one({"_id": ObjectId(item_id)})
    return render_template('editschedule.html',
                           schedule=mongo.db.schedule.find(), item=the_item)


@app.route('/update_item/<item_id>', methods=["POST"])
def update_item(item_id):
    schedule = mongo.db.schedule
    schedule.update({'_id': ObjectId(item_id)},
                    {
                        'day': request.form.get('day'),
                        'morning': request.form.get('morning'),
                        'afternoon': request.form.get('afternoon'),
                        'dinner': request.form.get('dinner'),
                        'dinner_name': request.form.get('dinner_name'),
                        'evening': request.form.get('evening'),
                    })
    return redirect(url_for('get_schedule'))


#@app.route('/update_item.morning/<item.morning_id>', methods=["POST"])
#def update_item.morning(item.morning_id):
    #schedule = mongo.db.schedule
    #schedule.update({'_id': ObjectId(item.morning_id)},
                  #  {
                  #      'morning': request.form.get('morning'),
                  #  })
   # return redirect(url_for('get_schedule'))


#@app.route('/delete_item/<item_id>')
#def delete_item(item_id):
    #mongo.db.schedule.remove({'_id': ObjectId(item_id)})
    #return redirect(url_for('get_schedule'))


@app.route('/')  # code from task manager mini-project to show list of expenses
@app.route('/get_expenses')
def get_expenses():
    expenses = mongo.db.expenses.find()
    #the_expense = mongo.db.expenses.find()
    total = 0

    
    # the_expense_e = mongo.db.expenses.find({ }, { amounts: 1 })
    # print("EXPENSES")
    # print(the_expense_e)
    # total = add_all_expenses(the_expense_e)
    return render_template("expenses.html", expenses=expenses,
                           total=total)


@app.route('/add_expense')  # from task manager mini-project to add expenses
def add_expense():
    the_expense = mongo.db.expenses.find()
    return render_template('addexpenses.html',
                           expenses=mongo.db.expenses.find(),
                           expense=the_expense)


@app.route('/insert_expense', methods=['POST'])  # from task mgr to add expense
def insert_expense():
    expenses = mongo.db.expenses
    #the_expense = mongo.db.expenses.find()
    expenses.insert_one(request.form.to_dict())
    return redirect(url_for('get_expenses'))


#@app.route('/edit_expense/<expense_id>')
#def edit_expense(expense_id):
   # the_expense = mongo.db.expenses.find_one({"_id": ObjectId(expense_id)})
   # return render_template('editexpenses.html',
                    #    expenses=mongo.db.expenses.find(), expense=the_expense)


@app.route('/edit_expense/<expense_id>')
def edit_expense(expense_id):
    the_expense = mongo.db.expenses.find_one({"_id": ObjectId(expense_id)})
    return render_template('editexpenses.html', expense=the_expense)


@app.route('/update_expense/<expense_id>', methods=["POST"])
def update_expense(expense_id):
    expenses = mongo.db.expenses
    the_expense = mongo.db.expenses.find_one({"_id": ObjectId(expense_id)})
    expenses.update({'_id': ObjectId(expense_id)},
                    {
                        'exp_name': request.form.get('exp_name'),
                        'date': request.form.get('date'),
                        'amount': request.form.get('amount'),
                        'person': request.form.get('person'),
                        'notes': request.form.get('notes')
                    })
    return redirect(url_for('get_expenses'))


@app.route('/delete_expense/<expense_id>')  # from task mgr to delete expense
def delete_expense(expense_id):
    mongo.db.expenses.remove({'_id': ObjectId(expense_id)})
    return redirect(url_for('get_expenses'))


#def add_all_expenses(list_amounts):
   # total = sum(list_amounts)
    # return total


if __name__ == '__main__':
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT")),
            debug=True)

# appbuilder = AppBuilder(app, db.session, base_template='mybase.html')
