from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # this a function to create other pages
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a')as database:
#         name = data["name"]
#         email = data["email"]
#         budget = data["budget"]
#         creator = data["creator"]
#         message = data["message"]
#         file = database.write(f'\n{name},{email},{creator},{budget},{message}')


def write_to_csv(data):
    with open('hirecreator.csv', mode='a', newline='')as database2:
        
        fullname = data["fullname"]
        email = data["email"]
        budget = data["budget"]
        creator = data["creator"]
        phone = data["phone"]
        location = data["location"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fullname, email,creator,budget, location, phone, message])

def write_to_csv1(data):
    with open('support.csv', mode='a', newline='')as database3:
        
        fullname = data["fullname"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        location = data["location"]
        csv_writer1 = csv.writer(database3, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer1.writerow([fullname, email, phone, location, message])

def write_to_csv2(data):
    with open('application.csv', mode='a', newline='')as database4:
        
        fullname = data["fullname"]
        email = data["email"]
        website = data["website"]
        creator = data["creator"]
        notice = data["notice"]
        phone = data["phone"]
        location = data["location"]
        message = data["message"]
        csv_writer2 = csv.writer(database4, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer2.writerow([fullname, email, website, creator, notice, location, phone,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
    else:
        return 'something went wrong'


@app.route('/submit_formed', methods=['POST', 'GET'])
def submit_formed():
    if request.method == 'POST':
            data=request.form.to_dict()
            write_to_csv2(data)
            return redirect('/thanks.html')
    else:
        return 'something went wrong'


@app.route('/submit_formed2', methods=['POST', 'GET'])
def submit_formed2():
    if request.method == 'POST':
            data=request.form.to_dict()
            write_to_csv1(data)
            return redirect('/thanks.html')
    else:
        return 'something went wrong'

 # @app.route('/favicon.ico')
 # def hello_world():
 #     return render_template('index.html')
