#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *second_half, *mid_node;
	int is_palindrome = 1;

	slow = fast = prev_slow = *head;
	mid_node = NULL;

	/* Find the middle node of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	/* Handle the case when the list has odd number of elements */
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	second_half = slow;
	prev_slow->next = NULL;
	reverse_list(&second_half);

	/* Compare the first half with the reversed second half */
	is_palindrome = compare_lists(*head, second_half);

	/* Reconstruct the original list by reversing the second half again */
	reverse_list(&second_half);

	/* If the list had an odd number of elements, link back the middle node */
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 *
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 *
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;

		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}
