#include <stdio.h>

#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);
/**
 * main - main method
 * Return: 0 for success
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(1);
	}
	infinite_while();
	return (0);
}

/**
 * infinte_while - infinite sleep
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
		sleep (1);
	return (0);
}
