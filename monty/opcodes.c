#include "main.h"

void push_monty(stack_t **stack, unsigned int line_number)
{
	stack_t *newNode;
	unsigned int j = 1;
	int n;
	char *errMsg1 = ": usage: push integer\n";

	if (!(glob.op_arg))
		free_stack(stack, errMsg1);
	if (!((glob.op_arg[0] >= '0' && glob.op_arg[0] <= '9')
	|| glob.op_arg[0] == '-'))
		free_stack(stack, errMsg1);
	while (glob.op_arg[j])
	{
		if (isdigit(glob.op_arg[j]) == 0)
			free_stack(stack, errMsg1);
		j++;
	}
	newNode = malloc(sizeof(stack_t));
	n = atoi(glob.op_arg);
	newNode->n = n;
	newNode->prev = NULL;
	newNode->next = *stack;
	if (*stack != NULL)
		(*stack)->prev = newNode;
	*stack = newNode;
	(void) line_number;
}

void mul_monty(stack_t **stack, unsigned int line_number)
{
	stack_t *tmpNode;
	char *errMsg1 = ":can't mul, stack too short\n";

	if (!(*stack))
		free_stack(stack, errMsg1);
	if (!((*stack)->next))
		free_stack(stack, errMsg1);
	tmpNode = (*stack);
	tmpNode->next->n *= tmpNode->n;
	(*stack) = (*stack)->next;
	(*stack)->prev = NULL;
	free(tmpNode);
	(void) line_number;
}

void pchar_monty(stack_t **stack, unsigned int line_number)
{
	char pchar;
	char *errMsg1 = ": can't pchar, stack empty\n";
	char *errMsg2 = ": can't pchar, value out of range\n";

	if (!(*stack))
		free_stack(stack, errMsg1);
	if ((*stack)->n < 0 || (*stack)->n > 127)
		free_stack(stack, errMsg2);
	pchar = (*stack)->n;
	printf("%c\n", pchar);
	(void) line_number;
}

void pstr_monty(stack_t **stack, unsigned int line_number)
{
	stack_t *tmpNode;

	tmpNode = (*stack);
	while (tmpNode && tmpNode->n > 0 && tmpNode->n < 128)
	{
		printf("%c", tmpNode->n);
		tmpNode = tmpNode->next;
	}
	printf("\n");
	(void) line_number;
}

void rotl_monty(stack_t **stack, unsigned int line_number)
{
	stack_t *tmpNode, *topNode, *botNode;

	if (!(*stack))
		return;
	if (!((*stack)->next))
		return;
	botNode = (*stack);
	topNode = (*stack)->next;
	tmpNode = (*stack);
	while (tmpNode->next)
		tmpNode = tmpNode->next;
	tmpNode->next = botNode;
	topNode->prev = NULL;
	(*stack) = topNode;
	botNode->prev = tmpNode;
	botNode->next = NULL;
	(void) line_number;
}
