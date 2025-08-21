/*
 * Day 1 Practice - C Basics
 * Date: 2024-12-19
 * Goals: Complete Week 1 Day 1 exercises
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
    printf("=== Exercise 1: Basic Array Operations ===\n");
    
    // Create and initialize arrays
    int arr1[5] = {1, 2, 3, 4, 5};
    double arr2[10];
    int i;
    
    // Initialize arr2 with values
    for (i = 0; i < 10; i++) {
        arr2[i] = i * 0.5;
    }
    
    // Print arrays
    printf("Array 1: ");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");
    
    printf("Array 2: ");
    for (i = 0; i < 10; i++) {
        printf("%.1f ", arr2[i]);
    }
    printf("\n");
    
    // Calculate sum of arr1
    int sum = 0;
    for (i = 0; i < 5; i++) {
        sum += arr1[i];
    }
    printf("Sum of Array 1: %d\n", sum);
    
    printf("Exercise 1 completed.\n\n");
}

void exercise_2(void) {
    printf("=== Exercise 2: Simple Signal Generation ===\n");
    
    const int N = 100;
    double signal[N];
    double t[N];
    int i;
    
    // Generate time array
    for (i = 0; i < N; i++) {
        t[i] = i * 0.01; // 0.01 second intervals
    }
    
    // Generate sine wave signal
    for (i = 0; i < N; i++) {
        signal[i] = sin(2 * M_PI * 5 * t[i]); // 5 Hz sine wave
    }
    
    // Print first 10 values
    printf("Time array (first 10): ");
    for (i = 0; i < 10; i++) {
        printf("%.2f ", t[i]);
    }
    printf("\n");
    
    printf("Signal array (first 10): ");
    for (i = 0; i < 10; i++) {
        printf("%.3f ", signal[i]);
    }
    printf("\n");
    
    // Calculate signal statistics
    double sum = 0.0, mean, variance = 0.0;
    for (i = 0; i < N; i++) {
        sum += signal[i];
    }
    mean = sum / N;
    
    for (i = 0; i < N; i++) {
        variance += (signal[i] - mean) * (signal[i] - mean);
    }
    variance /= N;
    
    printf("Signal mean: %.4f\n", mean);
    printf("Signal variance: %.4f\n", variance);
    
    printf("Exercise 2 completed.\n\n");
}

void exercise_3(void) {
    printf("=== Exercise 3: Basic DSP Operations ===\n");
    
    const int N = 50;
    double input[N], output[N];
    int i;
    
    // Generate input signal with noise
    for (i = 0; i < N; i++) {
        // Clean signal + noise
        input[i] = sin(2 * M_PI * 0.1 * i) + 0.1 * ((double)rand() / RAND_MAX - 0.5);
    }
    
    // Simple moving average filter
    const int window = 5;
    for (i = 0; i < N; i++) {
        double sum = 0.0;
        int count = 0;
        
        // Apply moving average
        for (int j = -window/2; j <= window/2; j++) {
            int idx = i + j;
            if (idx >= 0 && idx < N) {
                sum += input[idx];
                count++;
            }
        }
        output[i] = sum / count;
    }
    
    // Print results
    printf("Input signal (first 10): ");
    for (i = 0; i < 10; i++) {
        printf("%.3f ", input[i]);
    }
    printf("\n");
    
    printf("Filtered signal (first 10): ");
    for (i = 0; i < 10; i++) {
        printf("%.3f ", output[i]);
    }
    printf("\n");
    
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
