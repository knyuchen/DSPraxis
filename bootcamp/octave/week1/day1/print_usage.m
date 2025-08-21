function print_usage()
    fprintf('Usage: octave main.m [OPTIONS]\n');
    fprintf('Options:\n');
    fprintf('  --exercise <num>  Run specific exercise (1, 2, or 3)\n');
    fprintf('  -e <num>          Run specific exercise (1, 2, or 3)\n');
    fprintf('  --all             Run all exercises\n');
    fprintf('  -a                Run all exercises\n');
    fprintf('  --help            Show this help message\n');
    fprintf('  -h                Show this help message\n');
    fprintf('\nExamples:\n');
    fprintf('  octave main.m                    # Run all exercises\n');
    fprintf('  octave main.m --exercise 1       # Run exercise 1 only\n');
    fprintf('  octave main.m -e 2               # Run exercise 2 only\n');
    fprintf('  octave main.m --all              # Run all exercises explicitly\n');
end
