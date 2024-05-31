from flask import Flask, jsonify
import random

# Create an instance of the Flask class. 
# The first argument is the name of the application's module or package.
# __name__ is a convenient way to get the name of the current module. 
# This is needed so that Flask knows where to look for resources like templates and static files.
app = Flask(__name__)

@app.route('/random', methods=['GET'])
def random_numbers():
    """
    Generate and return a list of 10 random integers between 1 and 100 as a JSON response.

    This function is a view function, which means it is called when a specific URL endpoint is accessed.
    It is mapped to the URL path '/random' and is configured to respond to HTTP GET requests.

    When this endpoint is accessed, the function performs the following steps:
    
    1. Initializes an empty list to store the random integers.
    2. Uses a list comprehension to generate 10 random integers.
       - The `random.randint(1, 100)` function is called 10 times, each time generating a random integer between 1 and 100 (inclusive).
       - The list comprehension iterates 10 times, as specified by `range(10)`, and collects each random integer in a list.
    3. Uses `jsonify` to convert the list of integers into a JSON response.
       - JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.
    4. Returns the JSON response to the client.

    Returns:
        Response: A Flask Response object containing a JSON array of 10 random integers.
                  This JSON array is automatically converted to a JSON string and sent to the client with a MIME type of 'application/json'.
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

    The debug mode provides the following features:
        - Automatic code reloading: The server automatically restarts when it detects code changes. This is particularly useful during development.
        - Interactive debugger: If an error occurs during a request, an interactive traceback is provided in the browser, allowing the developer to inspect variables and stack frames.
        
    The app.run() function starts the Flask development server. 
    The server listens for HTTP requests on the local machine (localhost) and the default port (5000).

    Arguments:
        debug (bool): A keyword argument that enables or disables debug mode.
                      When set to True, debug mode is enabled.
    """
    # app.run starts the Flask web server.
    # debug=True enables debug mode.
    app.run(debug=True)
