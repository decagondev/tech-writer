const express = require('express');

/**
 * Create an instance of an Express application.
 * Express is a minimal and flexible Node.js web application framework
 * that provides a robust set of features for web and mobile applications.
 */
const app = express();

/**
 * Define a route handler for GET requests to the /random endpoint.
 * This route generates and returns a list of 10 random integers between 1 and 100.
 *
 * @name /random
 * @function
 * @memberof module:express~app
 * @inner
 * @param {string} path - The path for which the middleware function is invoked.
 * @param {callback} middleware - The middleware function.
 */
app.get('/random', (req, res) => {
    /**
     * Generate a list of 10 random integers between 1 and 100.
     * Array.from() creates a new array from an array-like or iterable object.
     * The second argument is a map function that is called on every element of the array.
     * Math.random() generates a floating-point number between 0 (inclusive) and 1 (exclusive).
     * Math.floor() rounds down to the nearest integer.
     *
     * @returns {number[]} An array of 10 random integers between 1 and 100.
     */
    const randomList = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100) + 1);

    /**
     * Send the list as a JSON response.
     * res.json() converts the input to a JSON string and sets the appropriate response headers.
     *
     * @param {Object} body - The response body.
     * @returns {void}
     */
    res.json(randomList);
});

/**
 * Start the server and listen on port 3000.
 * The app.listen() function binds and listens for connections on the specified host and port.
 *
 * @param {number} port - The port number on which the server will listen.
 * @param {string} [host=localhost] - The host on which the server will listen.
 * @param {function} [callback] - A callback function that is called once the server starts listening.
 * @returns {http.Server} The HTTP server instance.
 */
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
