#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int main(int argc, char **argv) {
    int myData[5] = {0, 1, 2, 3, 4};

    if (argc >= 2) {
        char *endptr;
        errno = 0;
        long index = strtol(argv[1], &endptr, 10);

        // Check for integer overflow and invalid input
        if (errno == ERANGE || *endptr != '\0' || index < 0 || index >= 5) {
            fprintf(stderr, "Invalid index\n");
            return 1;
        }

        printf("%d", myData[(int)index]);
    } else {
        fprintf(stderr, "Usage: %s <index>\n", argv[0]);
        return 1;
    }

    return 0;
}