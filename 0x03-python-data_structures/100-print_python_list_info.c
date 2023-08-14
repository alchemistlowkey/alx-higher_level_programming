#include <stdio.h>
#include "Python.h"
/**
 * print_python_list_info - prints info about python list
 * @p: a pointer
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len, allocated, i;
	const char *type;

	len = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < len; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
