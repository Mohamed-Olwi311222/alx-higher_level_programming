#include "lists.h"

/**
 * is_palindrome - checks if the list is a palindrome or not
 * @head: head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy = NULL;
	listint_t *orig = *head;
	listint_t *ptr = NULL;

	copy = copyList(*head);
	reverseList(&copy);
	ptr = copy;
	while (orig != NULL)
	{
		if (orig->n != ptr->n)
		{
			return (0);
		}
		ptr = ptr->next;
		orig = orig->next;
	}
	free_listint(copy);
	return (1);
}

/**
 * copyList - copy a linked list
 * @original: original list
 * Return: the head of the new list
 */
listint_t *copyList(listint_t *original)
{
	listint_t *copy = NULL;

	if (!original)
	{
		return (NULL);
	}
	while (original != NULL)
	{
		add_nodeint_end(&copy, original->n);
		original = original->next;
	}
	return (copy);
}

/**
 * reverseList - reverse a linked list
 * @head: head of the list to reverse
 */
void reverseList(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	if (!head)
		return;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
}

