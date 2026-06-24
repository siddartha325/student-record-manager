from flask import Flask, render_template, request
import re

app = Flask(__name__)

FILE_NAME = "students.txt"

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_student():
    try:
        roll = request.form['roll']
        name = request.form['name']
        email = request.form['email']

        if not validate_email(email):
            return "Invalid Email Format!"

        with open(FILE_NAME, "a") as file:
            file.write(f"{roll},{name},{email}\n")

        return "Student Record Saved Successfully!"

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)