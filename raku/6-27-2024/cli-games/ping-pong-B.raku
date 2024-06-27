#ping-pong-B.raku
# Simple interactive CLI Ping-Pong game in Raku

sub start-ping-pong-game {
    my $continue = True;
    my $player-turn = True;

    say "Welcome to the Ping-Pong game!";
    say "Type 'ping' to start. Type 'quit' to end the game anytime.";

    while $continue {
        if $player-turn {
            print "Your turn: ";
            my $input = get().trim.lc;

            if $input eq 'ping' || $input eq 'pong' {
                say "$input!";
                $player-turn = False;
            } elsif $input eq 'quit' {
                say "You quit the game. Goodbye!";
                $continue = False;
            } else {
                say "Invalid input. Type 'ping', 'pong', or 'quit'.";
            }
        } else {
            my $computer-response = rand < 0.5 ?? 'ping' !! 'pong';
            say "Computer: $computer-response!";
            $player-turn = True;
        }
    }
}

start-ping-pong-game();
