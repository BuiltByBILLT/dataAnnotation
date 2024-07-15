#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int myData[5] = {0, 1, 2, 3, 4};

    if (argc >= 2) {
        int index = atoi(argv[1]);
        printf("%d", myData[index]);
    }
}
    