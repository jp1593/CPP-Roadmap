/* A pointer is a variable that stores the memory address of another variable (or function). It points to the location of the variable in memory,
and it allows you to access or modify the value indirectly. Here’s a general format to declare a pointer:

    dataType *pointerName;

    & address of operator (establish the variable referenced to the pointer) *Arrays dont need to have this
    * dereferference operator (gets value that reference the variable with the pointer)

*/

#include <iostream>

// Function pointer
int add(int a, int b)
{
    std::cout << (a + b);
    return (a + b);
}

int main()
{
    int num = 10;
    int *ptr = &num;  // Pointer 'ptr' now points to the memory address of 'num'
    int value = *ptr; // Value now contains the value of the variable that 'ptr' points to (i.e., 10)

    std::cout << value << "\n";

    // Pointer function
    int (*funcptr)(int, int) = add; // Pointer 'funcptr' now points to the functions 'add'
    funcptr(4, 5);                  // Return 9

    return 0;
}