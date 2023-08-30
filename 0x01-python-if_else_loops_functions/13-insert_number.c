#include "lists.h"
/**
 * create_new_node - creates a new node
 * @number: number to store in it
 * Return: the address of the newnode or NULL if failed
 */
listint_t *create_new_node(int number)
{
	listint_t *newnode = malloc(sizeof(*newnode));

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	return (newnode);
}
/**
 * insert_node - insert a node in a sorted linked list
 * @head: head of the list
 * @number: number to insert
 * Return: the address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = NULL, *inserted_node = NULL;

	if (head == NULL || *head == NULL)
		return (NULL);

	ptr = *head;
	while (ptr != NULL && ptr->n < number)
	{
		inserted_node = ptr;
		ptr = ptr->next;
	}

	ptr = inserted_node;
	inserted_node = create_new_node(number);
	inserted_node->next = ptr->next;
	ptr->next = inserted_node;

	return (inserted_node);
}
