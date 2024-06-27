#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <string>

// Function to generate a list of 10 random numbers
std::vector<int> generate_random_numbers() {
    std::vector<int> numbers;
    for (int i = 0; i < 10; ++i) {
        numbers.push_back(rand() % 101);  // Random number between 0 and 100
    }
    return numbers;
}

// Function to convert vector of numbers to JSON format string
std::string to_json(const std::vector<int>& numbers) {
    std::string json = "[";
    for (size_t i = 0; i < numbers.size(); ++i) {
        json += std::to_string(numbers[i]);
        if (i != numbers.size() - 1) {
            json += ", ";
        }
    }
    json += "]";
    return json;
}

int main() {
    // Initialize random seed
    std::srand(std::time(0));

    // Generate random numbers
    std::vector<int> random_numbers = generate_random_numbers();

    // Convert to JSON
    std::string json_output = to_json(random_numbers);

    // Output HTTP headers and JSON content
    std::cout << "Content-Type: application/json\n\n";
    std::cout << json_output << std::endl;

    return 0;
}
