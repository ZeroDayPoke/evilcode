#include "main.h"

void op_fun_res(stack_t **stack)
{
	unsigned int i;
	char *errMsg1 = "!: unknown instruction ";

	instruction_t betty[] = {
		{"push", push_monty},
		{"mul", mul_monty},
		{"pstr", pstr_monty},
		{"pchar", pchar_monty},
		{"rotl", rotl_monty},
		{NULL, NULL}
	};

	i = 0;
	while (betty[i].opcode != NULL)
	{
		if (strcmp(glob.op_code, betty[i].opcode) == 0)
		{
			betty[i].f(stack, glob.op_line);
			return;
		}
		i++;
	}
	free_stack(stack, errMsg1);
}
