from flask import Flask, jsonify
import random

# Create an instance of the Flask class. The first argument is the name of the application's module or package.
# __name__ is a convenient way to get the name of the current module. This is needed so that Flask knows where to look
# for resources like templates and static files.
app = Flask(__name__)

@app.route('/random', methods=['GET'])
def random_numbers():
    """
    Generate and return a list of 10 random integers between 1 and 100 as a JSON response.

    This view function is mapped to the URL path '/random' and is accessible via HTTP GET requests.
    When a GET request is received, the function performs the following steps:
    1. Generates a list of 10 random integers between 1 and 100.
    2. Converts the list of integers to a JSON formatted response.
    3. Returns the JSON response to the client.

    Returns:
        Response: A Flask Response object containing a JSON array of 10 random integers.
    """
    # Generate a list of 10 random integers between 1 and 100 using a list comprehension.
    # random.randint(1, 100) generates a random integer between 1 and 100, inclusive.
    # The list comprehension runs this function 10 times (for _ in range(10)), collecting the results into a list.
    random_list = [random.randint(1, 100) for _ in range(10)]
    
    # jsonify is a Flask utility that converts the list of integers to a JSON response.
    # JSON (JavaScript Object Notation) is a lightweight data interchange format.
    # It is easy for humans to read and write, and easy for machines to parse and generate.
    return jsonify(random_list)

if __name__ == '__main__':
    """
    Entry point of the Flask application.

    This block ensures that the Flask web server is run only when the script is executed directly (not imported as a module).
    When run, the Flask application starts a local development server in debug mode.
    Debug mode:
        - Automatically restarts the server upon detecting code changes.
        - Provides a detailed interactive debugger for errors.
    """
    # app.run starts the Flask web server.
    # debug=True enables debug mode.
    app.run(debug=True)
