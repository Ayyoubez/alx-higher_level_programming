#include "lists.h"

/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to the head of the list.
 *
 * Return: Pointer to the reversed list.
 */

void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
}

/**
* is_palindrome - Check the linked list type
* @head: parameter
* Return: 1 or 0
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *temp = *head;
	listint_t *dupl = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dupl = slow->next;
			break;
		}
		if (!fast->next)
		{
			dupl = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&dupl);

	while (dupl && temp)
	{
		if (temp->n == dupl->n)
		{
			dupl = dupl->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dupl)
		return (1);
	return (0);
}
