#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 150

/**
 * main - fork fun
 * Return: Always 0
 */
int main(void)
{
	int pid = fork();
	char buf[BUF_SIZE];
	int print_count;

	switch (pid)
	{
	case -1:
		perror("fork failed");
		exit(1);
	case 0:
		/* When fork() returns 0, we are in the child process. */
		print_count = 10;
		sprintf(buf, "child process: pid = %d", pid);
		break;
    default: /* + */
		/* When fork() returns a positive number, we are in the parent process */
		/* (the fork return value is the PID of the newly created child process) */
		print_count = 5;
		sprintf(buf, "parent process: pid = %d", pid);
		break;
	}
	for (; print_count > 0; print_count--)
	{
		puts(buf);
		sleep(1);
	}
	exit(0);
}
