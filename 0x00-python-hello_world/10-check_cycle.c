#include "lists.h"

/**
  * check_cycle - function that checks if a singly linked list has a cycle.
  * @list: pointer to the first element.
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle.
  */
int check_cycle(listint_t *list)
{
	listint_t *now = list;
	listint_t *later = list;

	if (!list)
		return (0);

	while (now && later && later->next)
	{
		now = now->next;
		later = later->next->next;
		if (now == later)
			return (1);
	}

	return (0);
}
