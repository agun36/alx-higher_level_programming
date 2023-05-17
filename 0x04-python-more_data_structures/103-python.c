#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - Prints info about a Python bytes object
 * @p: A PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
        PyBytesObject *bytes = (PyBytesObject *)p;
        Py_ssize_t i, size;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
            printf("  [ERROR] Invalid Bytes Object\n");
            return;
            
        }
        size = PyBytes_Size(p);
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", bytes->ob_sval);
        printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
        for (i = 0; i <= size && i < 10; i++)
        printf("%02x%c", bytes->ob_sval[i] & 0xff, i == 9 ? '\n' : ' ');
}

/**
 * print_python_list - Prints info about a Python list object
 * @p: A PyObject list object
 */
void print_python_list(PyObject *p)
{
        PyObject *item;
        PyListObject *list = (PyListObject *)p;
        Py_ssize_t i, size;
        
        size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", list->allocated);
        for (i = 0; i < size; i++)
        {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
            if (PyBytes_Check(item))
            print_python_bytes(item);
            
        }
}
