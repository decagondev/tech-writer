const { Sequelize, DataTypes } = require('sequelize');

// Initialize Sequelize to use SQLite
const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: 'database.sqlite'
});

// Define the Todo model
const Todo = sequelize.define('Todo', {
    // Unique identifier for the Todo item
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true
    },
    // The title of the Todo item
    title: {
        type: DataTypes.STRING,
        allowNull: false
    },
    // Indicates whether the Todo item is completed
    completed: {
        type: DataTypes.BOOLEAN,
        defaultValue: false
    }
});

module.exports = { sequelize, Todo };
