% Day 1 Practice - Octave Basics
% Date: 2024-12-19
% Goals: Complete Week 1 Day 1 exercises

% Clear workspace and command window
clear all;
close all;
clc;

% Parse command line arguments (simple approach)
arg_list = argv();
exercise_num = 0;
run_all = false;

if length(arg_list) > 0
    if strcmp(arg_list{1}, '--exercise') || strcmp(arg_list{1}, '-e')
        if length(arg_list) > 1
            exercise_num = str2num(arg_list{2});
        end
    elseif strcmp(arg_list{1}, '--all') || strcmp(arg_list{1}, '-a')
        run_all = true;
    elseif strcmp(arg_list{1}, '--help') || strcmp(arg_list{1}, '-h')
        print_usage;
        return;
    end
end

% Run exercises based on arguments
if exercise_num > 0
    switch exercise_num
        case 1
            exercise_1;
        case 2
            exercise_2;
        case 3
            exercise_3;
        otherwise
            fprintf('Error: Invalid exercise number. Use 1, 2, or 3.\n');
            return;
    end
elseif run_all
    exercise_1;
    exercise_2;
    exercise_3;
else
    % Default: run all exercises
    exercise_1;
    exercise_2;
    exercise_3;
end