from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)
temp = {}
@app.route('/')
def home():
    return redirect(url_for('calculate'))

@app.route('/marks_submission', methods=['GET', 'POST']) # don't forget to include the full path of the url with marks_submission to the form in marks.html file
def calculate():
    if request.method == 'POST':
        student_name = request.form['nm']
        phy_marks = int(request.form['phy'])
        chem_marks = int(request.form['chem'])
        math_marks = int(request.form['math'])
        avg_marks = round((phy_marks+chem_marks+math_marks) / 3, 3)
        temp[student_name] = avg_marks
        return render_template('avg_result.html', result=temp) 
    else:
        return render_template('marks.html') # can just mention this line within @app.route('/')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
