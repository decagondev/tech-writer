#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate and print a list of 20 random numbers in JSON format
void generate_random_numbers() {
    printf("Content-Type: application/json\n\n");

    printf("[");
    for (int i = 0; i < 20; i++) {
        int random_number = rand() % 100 + 1;
        printf("%d", random_number);
        if (i < 19) {
            printf(", ");
        }
    }
    printf("]\n");
}

int main() {
    // Initialize random number generator
    srand(time(NULL));

    // Generate and output the list of random numbers
    generate_random_numbers();

    return 0;
}
