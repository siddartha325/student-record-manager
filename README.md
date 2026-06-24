# Student Record Manager

A simple web-based Student Record Manager built using **Python Flask**, **HTML**, and **CSS**.

## Features

* Add Student Records
* Email Validation using Regular Expressions (Regex)
* Save Student Data to Local File (`students.txt`)
* Exception Handling
* Simple and Responsive User Interface
* Flask Backend Integration

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Regular Expressions (Regex)

## Project Structure

```
StudentRecordManager/
│
├── app.py
├── students.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-record-manager.git
cd student-record-manager
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

## How It Works

1. Enter Roll Number, Student Name, and Email.
2. Email is validated using Regex.
3. If the email is valid, student details are stored in `students.txt`.
4. If invalid input is provided, an error message is displayed.
5. Records are saved locally and are not displayed on the webpage.

## Email Validation Pattern

```python
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
```

## Sample Record

```
23810548,Ravuri Siddartha,siddartharavuri@gmail.com
```

## Learning Outcomes

* Flask Web Development
* File Handling in Python
* Form Processing
* Regex Validation
* Exception Handling
* Frontend and Backend Integration

## Author

**Ravuri Siddartha**

B.Tech – Computer Science and Engineering

Velagapudi Ramakrishna Siddhartha Engineering College

```
```
