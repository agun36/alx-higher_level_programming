#include <Python.h>
#include <stdio.h>
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;
    const char *type;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        type = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char byte;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %zd bytes: ", size <= 10 ? size : 10);
    for (i = 0; i < (size <= 10 ? size : 10); i++)
    {
        byte = *(str + i);
        printf("%02x%s", byte, i == (size <= 10 ? size - 1 : 9) ? "\n" : " ");
    }
}
