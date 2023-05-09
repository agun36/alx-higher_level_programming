#include "lists.h"
#include <stddef.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head node of the list
 * @number: the number to be inserted
 * Return: the address of the new node or NULL if it fails
 **/
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new_node, *temp;

        new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
                return (NULL);

        new_node->n = number;
        if (*head == NULL || (*head)->n >= new_node->n)
        {
                new_node->next = *head;
                *head = new_node;
                return (new_node);
        }
        else
        {
                temp = *head;
                while (temp->next != NULL && temp->next->n < new_node->n)
                        temp = temp->next;
                new_node->next = temp->next;
                temp->next = new_node;
        }

        return (new_node);
}
