from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/cloth')
def get_cloth():
    data = [{'name': 'Jacket0', 'url': 'http://127.0.0.1:5000/cloth/jacket'},
            {'name': 'Jacket1', 'url': 'http://127.0.0.1:5000/cloth/jacket'},
            {'name': 'Jacket2', 'url': 'http://127.0.0.1:5000/cloth/jacket'}]
    return render_template('cloth.html', data=data)


@app.route('/cloth/jacket')
def get_cloth_jacket():
    data = {'name': 'Jacket012', 'price': '20000', 'origin_country': 'China'}
    return render_template('jacket.html', data=data)


@app.route('/shoes/shoes')
def get_shoes_shoes():
    data = {'name': 'Shoes012', 'price': '10000', 'origin_country': 'USA'}
    return render_template('jacket.html', data=data)


@app.route('/shoes')
def get_shoes():
    data = [{'name': 'Shoes0', 'url': 'http://127.0.0.1:5000/shoes/shoes'},
            {'name': 'Shoes1', 'url': 'http://127.0.0.1:5000/shoes/shoes'},
            {'name': 'Shoes2', 'url': 'http://127.0.0.1:5000/shoes/shoes'}]
    return render_template('shoes.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
