from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

def data_cleaning(sent, lang='english', stemmer='porter'): # porter, lancaster, snowball
    from nltk.corpus import stopwords
    from nltk import word_tokenize
    from nltk.stem import SnowballStemmer, PorterStemmer, LancasterStemmer
    ps = PorterStemmer()
    ls = LancasterStemmer()
    ss = SnowballStemmer(language=lang)
    swords = stopwords.words(lang)
    if stemmer == 'porter':
        stem_obj = ps
    elif stemmer == 'lancaster':
        stem_obj = ls
    elif stemmer == 'snowball':
        stem_obj = ss
    tokens = [stem_obj.stem(word) for word in word_tokenize(sent) if word.lower() not in swords and word.isalpha()]    # ignoring numerical values
    return tokens

import joblib
classifier_path = url_for('static', filename='models/classifier.model')
tfidf_path = url_for('static', filename='models/tfidf.model')
classifier = joblib.load(classifier_path)
tfidf = joblib.load(tfidf_path)
# routes
@app.route('/')
def home():
    return redirect(url_for('spam_detect'))


@app.route('/detect_spam', methods=['POST', 'GET'])
def spam_detect():
    
    if request.method == 'POST':
        data = dict(request.form)
        cleaned_data = tfidf.transform([data['message']]) # data['message']
        data['result'] = classifier.predict(cleaned_data)[0]
        return render_template('spam_result.html', data=data)
    else:
        return render_template('spam_detector.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=5009)