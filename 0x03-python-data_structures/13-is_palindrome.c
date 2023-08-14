#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - palindrome checker
 * @head: double pointer
 * Return: integer
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int j = 0, i = 0, *set = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	for (j = 0; tmp; j++)
	{
		tmp = tmp->next;
	}
	set = malloc(sizeof(int) * j);
	tmp = *head;
	while (tmp)
	{
		set[i++] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0; i < j / 2; i++)
	{
		if (set[i] != set[j - 1 - i])
		{
			free(set);
			return (0);
		}
	}
	free(set);
	return (1);
}
