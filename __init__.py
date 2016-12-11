from flask import Flask, render_template, request, redirect
from busbud import *

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post', methods=['POST'])
def post():
    bus = request.form['bus']
    stop = request.form['stop']
    thelist = data.pull()
    listoftimes = arrival.list(thelist, bus, stop)
    list = convertedtimes.converter(listoftimes)
    checkinput = Checkinput()
    if checkinput.checker(bus, stop) == False:
        return render_template('warning.html')
    else:
        return render_template('arrivals.html', list=list, bus=bus, stop=stop)

if __name__ == '__main__':
  app.run(debug=True)
