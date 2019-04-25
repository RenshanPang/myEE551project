from flask import Flask
from flask import render_template
from flask import request
import csv
with open('student imformation.csv', 'a', newline='') as f:
    csvwrite = csv.writer(f, dialect='excel')
    csvwrite.writerow(['Name', 'Sex', 'StudentID', 'Date'])
app = Flask(__name__)
@app.route('/')
def idex():
    return render_template('html1.html')
@app.route('/1')
def login():
    return render_template('html2.html')
@app.route('/2')
def information():
    name = request.args.get("name")
    sex = request.args.get("sex")
    studentid = request.args.get("StudentID")
    date = request.args.get("date")
    with open('student imformation.csv', 'a', newline='') as f:
        csvwrite = csv.writer(f, dialect='excel')
        csvwrite.writerow([name, sex, studentid, date])
    return render_template('html3.html')
app.run()
