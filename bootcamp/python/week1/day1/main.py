#!/usr/bin/env python3
"""
Day 1 Practice - NumPy Basics
Date: [Today's Date]
Goals: Learn basic NumPy operations, array creation, and simple DSP concepts
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse


def exercise_1():
    """Exercise 1: Basic NumPy Array Operations"""
    print("=== Exercise 1: Basic NumPy Array Operations ===")
    
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.linspace(0, 10, 11)
    arr3 = np.zeros(10)
    arr4 = np.ones(5)
    
    print(f"Array 1: {arr1}")
    print(f"Array 2 (0 to 10, 11 points): {arr2}")
    print(f"Array 3 (zeros): {arr3}")
    print(f"Array 4 (ones): {arr4}")
    
    # Basic operations
    print(f"\nArray 1 + 2: {arr1 + 2}")
    print(f"Array 1 * 3: {arr1 * 3}")
    print(f"Sum of Array 1: {np.sum(arr1)}")
    print(f"Mean of Array 1: {np.mean(arr1)}")


def exercise_2():
    """Exercise 2: Creating Simple Signals"""
    print("\n=== Exercise 2: Creating Simple Signals ===")
    
    # Create time array
    t = np.linspace(0, 1, 1000)
    
    # Create different signals
    sine_wave = np.sin(2 * np.pi * 5 * t)  # 5 Hz sine wave
    cosine_wave = np.cos(2 * np.pi * 3 * t)  # 3 Hz cosine wave
    square_wave = np.sign(np.sin(2 * np.pi * 2 * t))  # 2 Hz square wave
    
    print(f"Time array shape: {t.shape}")
    print(f"Sine wave shape: {sine_wave.shape}")
    print(f"First 5 values of sine wave: {sine_wave[:5]}")
    
    # Plot the signals
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, sine_wave)
    plt.title('5 Hz Sine Wave')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 2)
    plt.plot(t, cosine_wave)
    plt.title('3 Hz Cosine Wave')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 3)
    plt.plot(t, square_wave)
    plt.title('2 Hz Square Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    plt.tight_layout()
    plt.savefig('output/day1_signals.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("Signals plotted and saved to output/day1_signals.png")


def exercise_3():
    """Exercise 3: Basic DSP Operations"""
    print("\n=== Exercise 3: Basic DSP Operations ===")
    
    # Create a signal with noise
    t = np.linspace(0, 1, 1000)
    signal_clean = np.sin(2 * np.pi * 10 * t)
    noise = 0.1 * np.random.randn(1000)
    signal_noisy = signal_clean + noise
    
    # Calculate signal statistics
    print(f"Clean signal mean: {np.mean(signal_clean):.4f}")
    print(f"Noisy signal mean: {np.mean(signal_noisy):.4f}")
    print(f"Clean signal std: {np.std(signal_clean):.4f}")
    print(f"Noisy signal std: {np.std(signal_noisy):.4f}")
    
    # Simple filtering (moving average)
    window_size = 20
    filtered_signal = np.convolve(signal_noisy, np.ones(window_size)/window_size, mode='same')
    
    # Plot comparison
    plt.figure(figsize=(12, 6))
    plt.plot(t, signal_clean, label='Clean Signal', alpha=0.7)
    plt.plot(t, signal_noisy, label='Noisy Signal', alpha=0.5)
    plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
    plt.title('Signal Filtering Example')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('output/day1_filtering.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("Filtering example plotted and saved to output/day1_filtering.png")


def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day 1 DSP Practice - NumPy Basics')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3], 
                       help='Run specific exercise (1, 2, or 3)')
    parser.add_argument('--all', action='store_true', 
                       help='Run all exercises')
    
    args = parser.parse_args()
    
    if args.exercise:
        if args.exercise == 1:
            exercise_1()
        elif args.exercise == 2:
            exercise_2()
        elif args.exercise == 3:
            exercise_3()
    elif args.all:
        exercise_1()
        exercise_2()
        exercise_3()
    else:
        # Default: run all exercises
        exercise_1()
        exercise_2()
        exercise_3()


if __name__ == "__main__":
    main()
