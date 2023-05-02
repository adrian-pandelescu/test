from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# @app.route("/")
# def home_index():
#     return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file (data):
    with open('database.txt', mode='a') as database:
        fname = data["fname"]
        lname = data["lname"]
        email = data["email"]
        message = data["message"]
        file = database.write(f'\n{fname}, {lname}, {email}, {message}')
        
def write_to_csv (data):
    with open('database.csv', newline='', mode='a') as database2:
        fname = data["fname"]
        lname = data["lname"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fname,lname,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
    except:
        return 'did not save in database2'
    else:
        return 'something went wrong'

""" @app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/blog.html")
def blog():
    return render_template('blog.html')

@app.route("/single.html")
def single():
    return render_template('single.html')

@app.route("/careers.html")
def careers():
    return render_template('careers.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/technology.html")
def technology():
    return render_template('technology.html') """