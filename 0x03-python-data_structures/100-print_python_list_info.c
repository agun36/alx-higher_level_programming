#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject items.
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
    int list_s, all, i;
    PyObject *list_o;

    list_s = Py_SIZE(p);
    all = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", list_s);
    printf("[*] Allocated = %d\n", all);

    for (i = 0; i < list_s; i++)
    {
        printf("Element %d: ", i);

        list_o = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(list_o)->tp_name);
    }
}
