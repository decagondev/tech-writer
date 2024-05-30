from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def random_numbers():
    random_list = [random.randint(1, 100) for _ in range(10)]
    return jsonify(random_list)

if __name__ == '__main__':
    app.run(debug=True)
