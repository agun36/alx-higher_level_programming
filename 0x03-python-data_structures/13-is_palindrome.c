#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int length = 0;
	int count = 0;
	int result = 1;

	if (head == NULL || *head == NULL)
		return (1);

	while (current != NULL)
	{
		length++;
		current = current->next;
	}

	current = *head;

	while (count < length / 2)
	{
		if (current->n != current->next->n)
		{
			result = 0;
           		break;
		}
        current = current->next->next;
        count++;
	}

	return (result);
}
