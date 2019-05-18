from flask import Flask, render_template, url_for, flash, redirect, request,jsonify
from forms import *
import forms
import pandas as pd
import uuid
import log_in_check as check
import pymysql
from QueryEngine import QueryEngine
from flask_mail import Mail, Message
from random2 import randint
from datetime import datetime


qe = QueryEngine()
qe.setup_default()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a26ade032e7040309ba635818774a38b'
app.config['JAWSDB_URL'] = ''

@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/contact",methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route("/menu",methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.user.data
        password = form.password.data
        if check.login_check(username, password) == True:
            return redirect(url_for('manager_view'))
        else:
            flash('Invalid Account, Check Your Username and Password', 'danger')
    return render_template('login.html',form=form)


@app.route("/manager_view", methods=['GET', 'POST'])
def manager_view():
    return render_template('manager_view.html')


@app.route("/survey", methods=['GET','POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        sex = form.sex.data
        ethnicity = form.ethnicity.data
        age = form.age.data
        zipcode = form.zipcode.data

        qe.connect()
        query_string = f"INSERT INTO Survey(gender,ethnicity,age,zipcode,first_name) \
                                    VALUES('{sex}','{ethnicity}',{age},{zipcode},'{first_name}');"
        qe.do_query(query_string)
        qe.commit()
        qe.disconnect()
        return redirect(url_for('menu'))
        
    return render_template('survey.html',form=form)


# @app.route("/update_survey_data/<sex>/<ethnicity>/<age>/<zipcode>/<first_name>",methods=['GET','POST'])
# def update_survey_data(sex,ethnicity,age,zipcode,first_name):
#     qe.connect()
#     query_string = f"INSERT INTO Survey(gender,ethnicity,age,zipcode,first_name) VALUES('{sex}','{ethnicity}',{age},{zipcode},'{first_name}');"
#     qe.do_query(query_string)
#     qe.commit()
#     qe.disconnect()
#     return redirect(url_for('home'))

@app.route("/presentation", methods=['GET', 'POST'])
def presentation():
    return redirect("https://docs.google.com/presentation/d/1a4yvkCltQIFV3gebvXaQkMsHYrISS9xQNQg-WXjttIk/edit?ts=5cdf01ed#slide=id.gc6f80d1ff_0_23",code=302,Response=None)

@app.route("/live_report", methods=['GET', 'POST'])
def live_report():
    return redirect("https://public.tableau.com/profile/jinwoo.oh#!/vizhome/FinalProject_15581403306490/LiveAnalysis",
        code=302,Response=None)


@app.route("/static_report", methods=['GET', 'POST'])
def static_report():
    return redirect("https://public.tableau.com/profile/jinwoo.oh#!/vizhome/FinalProject_15581403306490/StaticAnalysis",
        code=302,Response=None)

@app.route("/cart", methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        response = request.get_json(force=True)  # parse as JSON
        keys = list(response.keys())
        order_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #check history transaction 
        transaction_id = randint(10, 999999)
        transaction_id_exist_check = check.transaction_check(transaction_id)
        while(transaction_id_exist_check):
            transaction_id = randint(10, 999999)
            transaction_id_exist_check = check.transaction_check(transaction_id)


        for i in range(len(keys)):
            food_id = keys[i]
            food_name = response[food_id][0]
            quantity = response[food_id][1]
            qe.connect()
            query_string = f"INSERT INTO Transaction VALUES({transaction_id},{food_id},'{food_name}',{quantity},'{order_time}');"
            qe.do_query(query_string)
            qe.commit()
            qe.disconnect()

        return redirect(url_for('survey'))
    else:
        return redirect(url_for('menu'))

if __name__ == '__main__':
    app.run(debug=True)





