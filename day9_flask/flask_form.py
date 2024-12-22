from flask import Flask, url_for, redirect, request, render_template

# Create a Flask application
app = Flask(__name__)  # can pass the path of the folder that holds static objects(images, js, css files) to the 'static_folder' parameter here.  'static' is the base folder name

@app.route('/')
def home():

    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm'] # all variables that are taken from the form are stored in a key value pair(dictionary) inside 'request' object
        return redirect(url_for('welcome', username=user))
    else:
        return render_template('basic_form.html') # for the GET method. or can just write a simple html page inside render_template

@app.route('/welcome/<username>')
def welcome(username):
    image_url = url_for('static', filename='images/jinwoo.jpg') # give name of the 'images' directory and then the filename, all within the preset 'static' folder
    return f'''<html><body><h2>Welcome {username}! Glad to have you here</h2>
                <style> img {{
                max-width: 100%;
                max-height: 95%;
                height: auto;
                    }}</style>
                <IMG src="{image_url}" alt='Wallpaper'></body></html>''' # example illustrating that we can pass html codes to the return statement here
# Run the application
if __name__ == "__main__":
    app.run(debug=True) # default port number is 5000, running on localhost