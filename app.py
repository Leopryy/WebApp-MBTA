"""
websites that take location name as input and return the nearest station name and if it is wheelchair accessible.
"""

from flask import Flask,render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def show_Location():
    if request.method == "POST":
        location = request.form['location']
        station, wheelchair_accessible = find_stop_near(location)
        return render_template('Index_output.html', location=station, wheelchair_accessible=wheelchair_accessible)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
