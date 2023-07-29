#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - Enter point that create zombie processes.
 *
 * Return: EXIT_SUCCESS everytime
 *
 **/
int main(void)
{
	int number_of_procs = 0;
	pid_t pid;

	while (number_of_procs < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
		{
			exit(EXIT_SUCCESS);
		}
		number_of_procs++;
	}
	infinite_while();


	return (EXIT_SUCCESS);
}

/**
 * infinite_while - Start an infinite loop
 *
 * Return: EXIT_SUCCESS everytime
 **/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
