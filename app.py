from flask import Flask, render_template, request, jsonify
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.get_json()
    algo = data.get('algorithm')
    array = data.get('array')

    if algo == 'bubble':
        steps = bubble_sort(array)
    elif algo == 'insertion':
        steps = insertion_sort(array)
    else:
        return jsonify({'error': 'Algorithme non reconnu'}), 400

    return jsonify({'steps': steps})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.get_json()
    algo = data.get('algorithm')
    array = data.get('array')

    if algo == 'bubble':
        steps = bubble_sort(array)
    elif algo == 'insertion':
        steps = insertion_sort(array)
    else:
        return jsonify({'error': 'Algorithme non reconnu'}), 400

    return jsonify({'steps': steps})

if __name__ == '__main__':
    app.run(debug=True)
