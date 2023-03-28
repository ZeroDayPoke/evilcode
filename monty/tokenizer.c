#include "main.h"

void tokentime(char *line, const char *delims, stack_t **stack_prime)
{
	glob.op_line++;
	glob.line_ref = line;
	glob.op_code = strtok(line, delims);
	if (!glob.op_code || glob.op_code[0] == '#')
		return;
	glob.op_arg = strtok(NULL, delims);
	op_fun_res(stack_prime);
}
