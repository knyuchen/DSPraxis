function exercise_3()
    fprintf('=== Exercise 3: Basic Signal Processing ===\n');
    
    % Generate noisy signal
    fs = 1000;
    t = 0:1/fs:1-1/fs;
    clean_signal = sin(2*pi*10*t);  % 10 Hz sine wave
    noise = 0.2 * randn(size(t));
    noisy_signal = clean_signal + noise;
    
    % Simple moving average filter
    window_size = 20;
    filtered_signal = zeros(size(noisy_signal));
    
    for i = 1:length(noisy_signal)
        start_idx = max(1, i - floor(window_size/2));
        end_idx = min(length(noisy_signal), i + floor(window_size/2));
        filtered_signal(i) = mean(noisy_signal(start_idx:end_idx));
    end
    
    % Calculate signal-to-noise ratio improvement
    noise_power_before = var(noisy_signal - clean_signal);
    noise_power_after = var(filtered_signal - clean_signal);
    snr_improvement = 10*log10(noise_power_before / noise_power_after);
    
    fprintf('Filter window size: %d samples\n', window_size);
    fprintf('SNR improvement: %.2f dB\n', snr_improvement);
    
    % Print some sample values
    fprintf('\nFirst 10 samples:\n');
    fprintf('Clean signal: ');
    fprintf('%.3f ', clean_signal(1:10));
    fprintf('\n');
    fprintf('Noisy signal: ');
    fprintf('%.3f ', noisy_signal(1:10));
    fprintf('\n');
    fprintf('Filtered signal: ');
    fprintf('%.3f ', filtered_signal(1:10));
    fprintf('\n');
    
    % Plot comparison (only if display is available)
    try
        figure(2);
        subplot(3,1,1);
        plot(t(1:300), clean_signal(1:300));
        title('Clean Signal');
        xlabel('Time (s)');
        ylabel('Amplitude');
        grid on;
        
        subplot(3,1,2);
        plot(t(1:300), noisy_signal(1:300));
        title('Noisy Signal');
        xlabel('Time (s)');
        ylabel('Amplitude');
        grid on;
        
        subplot(3,1,3);
        plot(t(1:300), filtered_signal(1:300));
        title('Filtered Signal');
        xlabel('Time (s)');
        ylabel('Amplitude');
        grid on;
        
        % Save figure
        print('output/day1_filtering.png', '-dpng');
        fprintf('Filtering comparison plotted and saved to output/day1_filtering.png\n');
    catch
        fprintf('Plotting skipped (no display available)\n');
    end
    
    fprintf('Exercise 3 completed.\n\n');
end
