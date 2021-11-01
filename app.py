from flask import Flask, render_template, request

import LinearRegression as lr

#create an instance of Flask
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    mk = 0
    if request.method == 'POST':
        mark = request.form['marks'] 
        mark_pred = lr.make_prediction(mark)
        mk = mark_pred

    return render_template('index.html', myMark = mk)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
 
