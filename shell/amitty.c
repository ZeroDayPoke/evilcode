#include <stdio.h>
#include <unistd.h>

int main()
{
    if (isatty(STDIN_FILENO))
        printf("Hi, i'm a TTY!\n");
    else
        printf("I am no a TTY :(\n");
    return (0);
}
