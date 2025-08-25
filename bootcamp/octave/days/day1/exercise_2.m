function exercise_2()
    fprintf('=== Exercise 2: Signal Generation ===\n');
    
    % Time vector
    fs = 1000;  % Sampling frequency
    t = 0:1/fs:1-1/fs;  % 1 second of data
    
    % Generate signals
    f1 = 50;   % 50 Hz
    f2 = 120;  % 120 Hz
    
    sine_wave = sin(2*pi*f1*t);
    cosine_wave = cos(2*pi*f2*t);
    square_wave = sign(sin(2*pi*f1*t));  % Simple square wave using sign function
    
    fprintf('Generated signals with %d samples\n', length(t));
    fprintf('Sampling frequency: %d Hz\n', fs);
    fprintf('Signal 1: %d Hz sine wave\n', f1);
    fprintf('Signal 2: %d Hz cosine wave\n', f2);
    fprintf('Signal 3: %d Hz square wave\n', f1);
    
    % Calculate statistics
    fprintf('\nSignal Statistics:\n');
    fprintf('Sine wave - Mean: %.4f, Std: %.4f\n', mean(sine_wave), std(sine_wave));
    fprintf('Cosine wave - Mean: %.4f, Std: %.4f\n', mean(cosine_wave), std(cosine_wave));
    fprintf('Square wave - Mean: %.4f, Std: %.4f\n', mean(square_wave), std(square_wave));
    
    % Plot signals (only if display is available)
    try
        figure(1);
        subplot(3,1,1);
        plot(t(1:200), sine_wave(1:200));
        title('50 Hz Sine Wave');
        xlabel('Time (s)');
        ylabel('Amplitude');
        grid on;
        
        subplot(3,1,2);
        plot(t(1:200), cosine_wave(1:200));
        title('120 Hz Cosine Wave');
        xlabel('Time (s)');
        ylabel('Amplitude');
        grid on;
        
        subplot(3,1,3);
        plot(t(1:200), square_wave(1:200));
        title('50 Hz Square Wave');
        xlabel('Time (s)');
        ylabel('Amplitude');
        grid on;
        
        % Save figure
        print('output/day1_signals.png', '-dpng');
        fprintf('Signals plotted and saved to output/day1_signals.png\n');
    catch
        fprintf('Plotting skipped (no display available)\n');
    end
    
    fprintf('Exercise 2 completed.\n\n');
end
