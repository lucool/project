from flask import Flask, render_template, jsonify

from HomeworkApp.db.tools import get_fruits,get_countries

app = Flask(__name__)


@app.route("/fruits/")
def fruits_view():
    fruits = get_fruits()
    return render_template('all_fruits.html',**locals())


@app.route("/go/")
def go_country():
    return render_template('country.html')


@app.route("/all/")
def all_countries():
    countries = get_countries()
    country_list = []
    for country in countries:
        country_dict = {
            "id":country[0],
            "name":country[1],
            "address":country[2]
        }
        country_list.append(country_dict)

    return jsonify(country_list)