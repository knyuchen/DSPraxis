/*
 * Day X Practice - [Topic]
 * Date: [Date]
 * Goals: [List of goals for this day]
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <unistd.h>
#include <getopt.h>

// Define M_PI if not already defined
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Function declarations
void exercise_1(void);
void exercise_2(void);
void exercise_3(void);
void print_usage(const char *program_name);

int main(int argc, char *argv[]) {
    int exercise_num = 0;
    int run_all = 0;
    int opt;
    
    // Parse command line arguments
    while ((opt = getopt(argc, argv, "e:ah")) != -1) {
        switch (opt) {
            case 'e':
                exercise_num = atoi(optarg);
                break;
            case 'a':
                run_all = 1;
                break;
            case 'h':
                print_usage(argv[0]);
                return 0;
            default:
                print_usage(argv[0]);
                return 1;
        }
    }
    
    // Run exercises based on arguments
    if (exercise_num > 0) {
        switch (exercise_num) {
            case 1:
                exercise_1();
                break;
            case 2:
                exercise_2();
                break;
            case 3:
                exercise_3();
                break;
            default:
                printf("Error: Invalid exercise number. Use 1, 2, or 3.\n");
                return 1;
        }
    } else if (run_all) {
        exercise_1();
        exercise_2();
        exercise_3();
    } else {
        // Default: run all exercises
        exercise_1();
        exercise_2();
        exercise_3();
    }
    
    return 0;
}

void exercise_1(void) {
    printf("=== Exercise 1: [Description] ===\n");
    // Your code here
    printf("Exercise 1 completed.\n\n");
}

void exercise_2(void) {
    printf("=== Exercise 2: [Description] ===\n");
    // Your code here
    printf("Exercise 2 completed.\n\n");
}

void exercise_3(void) {
    printf("=== Exercise 3: [Description] ===\n");
    // Your code here
    printf("Exercise 3 completed.\n\n");
}

void print_usage(const char *program_name) {
    printf("Usage: %s [OPTIONS]\n", program_name);
    printf("Options:\n");
    printf("  -e <num>    Run specific exercise (1, 2, or 3)\n");
    printf("  -a          Run all exercises\n");
    printf("  -h          Show this help message\n");
    printf("\nExamples:\n");
    printf("  %s           # Run all exercises\n", program_name);
    printf("  %s -e 1      # Run exercise 1 only\n", program_name);
    printf("  %s -a        # Run all exercises explicitly\n", program_name);
}
