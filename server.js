const express = require('express');

// Create an instance of an Express application
const app = express();

// Define a route handler for GET requests to the /random endpoint
app.get('/random', (req, res) => {
    // Generate a list of 10 random integers between 1 and 100
    const randomList = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100) + 1);

    // Send the list as a JSON response
    res.json(randomList);
});

// Start the server and listen on port 3000
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
