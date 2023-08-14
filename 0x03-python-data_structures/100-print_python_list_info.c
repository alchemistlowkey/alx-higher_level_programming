#include <stdio.h>
#include "Python.h"
/**
 * print_python_list_info - prints info about python list
 * @p: a pointer
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = NULL;
	size_t size = 0, i;
	const char *type = NULL;

	size = PyList_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", (signed long)(list->allocated));
	for  (i = 0; i < size; i++)
	{
		type = Py_TYPE(list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
