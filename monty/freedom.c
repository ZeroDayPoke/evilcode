#include "main.h"

void free_stack(stack_t **stack, char *msg)
{
	stack_t *scrubber;

	if (msg)
	{
		if (msg[0] == '!')
		{
			msg++;
			fprintf(stderr, "L%d%s%s\n", glob.op_line, msg, glob.op_code);
		}
		else
			fprintf(stderr, "L%d%s", glob.op_line, msg);
	}
	if (glob.line_ref)
		free(glob.line_ref);
	fclose(glob.file_ref);
	if (*stack)
	{
		while (*stack)
		{
			scrubber = (*stack)->next;
			free(*stack);
			(*stack) = scrubber;
		}
	}
	if (msg)
		exit(EXIT_FAILURE);
	else
		return;
}
