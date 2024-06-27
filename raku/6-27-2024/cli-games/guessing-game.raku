use v6;

sub MAIN {
    my $secret-number = 1 + (50.rand.Int);  # Random number between 1 and 50
    my $attempts = 0;
    
    say "Welcome to the Number Guessing Game!";
    say "I'm thinking of a number between 1 and 50.";
    
    loop {
        $attempts++;
        print "Enter your guess: ";
        my $guess = get();
        
        if $guess == $secret-number {
            say "Congratulations! You guessed the number in $attempts attempts.";
            last;
        }
        elsif $guess < $secret-number {
            say "Too low! Try again.";
        }
        else {
            say "Too high! Try again.";
        }
    }
}

MAIN();
