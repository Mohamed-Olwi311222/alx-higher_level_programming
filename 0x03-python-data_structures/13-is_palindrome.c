#include "lists.h"
/**
 * list_len - gets the length of the list
 * @head: head of the list
 * Return: the length of the list
*/
size_t list_len(listint_t *head)
{
	size_t len = 0;

	if (!head)
	{
		return (len);
	}
	while (head != NULL)
	{
		len++;
		head = head->next;
	}
	return (len);
}
/**
 * half_list - get the half of the list
 * @head: head of the list
 * @len: len of the list
 * Return: a pointer to the half of the list
*/
listint_t *half_list(listint_t *head, size_t len)
{
	size_t half = 0;
	listint_t *ptr = NULL;

	if (!head)
	{
		return (NULL);
	}
	while (head != NULL)
	{
		if (half == (len / 2) - 1)
		{
			if (len % 2 != 0)
			{
				ptr = head->next->next;
			}
			else
			{
				ptr = head->next;
			}
			head->next = NULL;
		}
		head = head->next;
		half++;
	}
	return (ptr);
}
/**
 * compareList - compare the two list
 * @head: original list
 * @length: length of the list
 * Return: 1 if identical else 0
*/
size_t compareList(listint_t *head, size_t length)
{
	listint_t *half = half_list(head, length);

	reverseList(&half);

	while (head != NULL)
	{
		if (head->n != half->n)
		{
			return (0);
		}
		head = head->next;
		half = half->next;
	}
	reverseList(&half);
	return (1);
}
/**
 * is_palindrome - checks if the list is a palindrome or not
 * @head: head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	size_t length = list_len(*head);
	size_t res = compareList(*head, length);

	return (res);
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

