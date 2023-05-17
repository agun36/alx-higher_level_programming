#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *object)
{
    char *string;
    long int size, i, limit;

    printf("[.] Bytes object info\n");
    if (!PyBytes_Check(object))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(object))->ob_size;
    string = ((PyBytesObject *)object)->ob_sval;

    printf("  Size: %ld\n", size);
    printf("  Trying string: %s\n", string);

    limit = (size >= 10) ? 10 : size + 1;

    printf("  First %ld bytes:", limit);

    for (i = 0; i < limit; i++)
    {
        if (string[i] >= 0)
            printf(" %02x", string[i]);
        else
            printf(" %02x", 256 + string[i]);
    }

    printf("\n");
}
/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *object)
{
    long int size, i;
    PyListObject *list;
    PyObject *item;

    size = ((PyVarObject *)(object))->ob_size;
    list = (PyListObject *)object;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        item = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
