####CREATING FLASK APPLICATION

##import flask
from flask import Flask,jsonify,render_template

##create flask instance
app=Flask(__name__)



##define function and route them
##@app.route('/')##exposing the function to the flask application ->app with the help of decorator

##def home():
##    return "Hello World !"




## '/','/about','/data' -> Three urls that I want to create->These urls are APIs itself
## And for these urls ,we create 3 endpoints.

#@app.route('/')
#def home():
#    return "Welcome to my Website."

#with the help of templates
#@app.route('/')
#def home_page():
#    name="Gayatri"
#    return render_template("index.html",name=name)

#@app.route('/', methods=['GET']) #GET method is already by default(no need to write it.)
#def home():
#    return "Hello World!"
@app.route('/',methods=["GET"])
def form():
    return render_template("form.html")

@app.route('/form',methods=['POST'])
def welcome():
    return "We have received your information Gayatri jiiii!!!"



@app.route('/about')
def about():

    #return plain string
    #data="Marvel Entertainment, LLC, a wholly-owned subsidiary of The Walt Disney Company, is one of the world's most prominent character-based entertainment companies, built on a proven library of more than 8,000 characters featured in a variety of media over eighty-five years. Marvel utilizes its character franchises in entertainment, licensing and publishing. For more information visit marvel.com. © 2026 MARVEL."
    #return data

    #returning HTML response
    return """<h1>About Us</h1><br>
              <h2>I am on a mission</h2><br>
              <h3>Thank You for visiting my website.</h3>"""
#about can contain large no. of paragraph,therefoore use templates


@app.route('/data')
def data():
    #dictionary itself in python is json format,but it is better to use jsonify function->provides with proper satndard formats
    user_data={"name":"ADITYA",
               "Age": 22}
    return jsonify(user_data)

##trigger the flask app
if __name__ =='__main__':
    app.run(debug=True) #using debug =True,helps in changing in real time,no need to close and then again run the application