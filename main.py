from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    f = open('database.txt', 'a')
    f.write('\n\n')
    f.write(str(datetime.today()))
    f.write('\n')
    for value in data:
        f.write(data[value])
        f.write('\n')
    f.close()


def write_to_csv(data):
    with open('database.csv', mode='a', newline='')as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
