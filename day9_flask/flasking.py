from flask import Flask, url_for, redirect

# Create a Flask application
app = Flask(__name__)  # an object of Flask class which is out WSGI application

# Define a route and its corresponding function
@app.route("/") # decorator to the function below. app.route(rule, options): Represents URL binding with the function
def home():
    return (f"<h1>Hello, Bluds</h1>")

@app.route("/about/<name>") # another URL + url binding
def about(name): # the name variable should be passed here
    return f"<h3>{name} blud has no rights.</h3>"


# ******************************************************************************************************************************
@app.route('/admin')
def admin():
    return "<h2>Welcome Admin</h2>"

@app.route("/guest/<name>")
def for_guest(guest_name):
    return f"<h3>Welcome, {guest_name}!</h3>"

@app.route("/user/<name>")
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('for_guest', guest_name=name)) # passing the name parameter received here to guest page
# **********************************************************************************************************************************

# Run the application
if __name__ == "__main__":
    app.run(debug=True, host='192.168.76.127', port=200) # default port number is 5000