#include "lists.h"

/**
 * insert_node - insert node in an ordered linked list
 * @head: the list passed in
 * @number: value of the new node
 * Return: address of new node or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)

{
	listint_t *current;
	listint_t *new;

	current = *head;
	if (!head)
		return NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (number < current->n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next)
		{
			if (number > current->next->n)
				current = current->next;
			else
				break;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
