#include<object.h>
#include<listobject.h>
#include<Python.h>

void print_python_list_info(PyObject *p);
{
	long int size = Pylist_Size(p);
	int i;
	PylistObject
