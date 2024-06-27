use Terminal::ANSIColor;

my $player1-score = 0;
my $player2-score = 0;
my $ball-position = 3; # Middle of the court
my $ball-direction = 1; # Moving right

sub clear-screen {
    print "\e[2J\e[H";  # ANSI escape codes to clear the screen and move the cursor to the top-left corner
}

sub draw-court {
    clear-screen();
    say " " x ($ball-position - 1) ~ "O" ~ " " x (7 - $ball-position);
    say "Player 1: $player1-score | Player 2: $player2-score";
}

loop {
    draw-court;

    my $input = prompt "Player " ~ ($ball-direction > 0 ?? 2 !! 1) ~ ": (l)eft or (r)ight? ";

    if $input eq 'l' {
        $ball-position -= 1 if $ball-direction > 0;
        $ball-position += 1 if $ball-direction < 0;
    } elsif $input eq 'r' {
        $ball-position += 1 if $ball-direction > 0;
        $ball-position -= 1 if $ball-direction < 0; 
    } else {
        say "Invalid input!";
        next;
    }

    # Keep ball within bounds
    $ball-position = 1 if $ball-position < 1;
    $ball-position = 7 if $ball-position > 7;

    # Check for scoring
    if ($ball-position == 1) {
        $player2-score += 1;
        say colored("Player 2 scores!", 'on_red');
        $ball-position = 4; # Reset ball slightly off-center
        $ball-direction = 1; # Serve to Player 1
        sleep 1;
    } elsif ($ball-position == 7) {
        $player1-score += 1;
        say colored("Player 1 scores!", 'on_green');
        $ball-position = 3; # Reset ball slightly off-center
        $ball-direction = -1; # Serve to Player 2
        sleep 1;
    } else {
        $ball-direction *= -1; # Change direction
    }

    # Check for win
    if ($player1-score >= 10) {
        say colored("Player 1 wins!", 'on_green');
        last;
    } elsif ($player2-score >= 10) {
        say colored("Player 2 wins!", 'on_red');
        last;
    }

    sleep 0.5;
}
