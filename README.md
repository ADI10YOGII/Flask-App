# Flask Web Application

A lightweight web application built using **Python** and the **Flask** micro-framework. This project demonstrates core Flask concepts including routing, template rendering, handling different request methods (`GET`, `POST`), and returning various response formats (`HTML`, `JSON`) based on your `main.py` implementation.

---

## Project Structure

```text
Flask App/
│
├── myenv/                  # Virtual environment
├── templates/              # HTML templates folder
│   ├── index.html          # Main template (with Jinja2 loops/conditionals)
│   └── form.html           # Form input template
├── main.py                 # Main Flask application file
└── requirements.txt        # Project dependencies


Core Concepts & Implementation
1. Flask Initialization
The application initializes the Flask instance:

app = Flask(__name__)


2. Routes & Endpoints (@app.route)
Routes map specific URLs to Python functions (endpoints):

GET Route & Form Rendering (/):
Serves the form.html template using render_template.

@app.route('/', methods=["GET"])
def form():
    return render_template("form.html")

@app.route('/', methods=["GET"])
def form():
    return render_template("form.html")

POST Route Form Handling (/form):
Handles form submission via the POST method.

@app.route('/form', methods=['POST'])
def welcome():
    return "We have received your information Gayatri jiiii!!!"

3. Different Response Formats
This project showcases multiple ways to return data from a route:

Raw HTML Response (/about):
Demonstrates returning raw HTML structure directly from a route function:

@app.route('/about')
def about():
    return """<h1>About Us</h1><br>
              <h2>I am on a mission</h2><br>
              <h3>Thank You for visiting my website.</h3>"""

JSON Responses (/data):
Uses Flask's built-in jsonify function to return structured dictionary data in standard JSON format:


@app.route('/data')
def data():
    user_data = {"name": "ADITYA", "Age": 22}
    return jsonify(user_data)
