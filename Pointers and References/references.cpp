/*
A reference is an alias for an existing variable, meaning it’s a different name for the same memory location. Unlike pointers,
references cannot be null, and they must be initialized when they are declared. Once a reference is initialized, it cannot be changed to refer to another variable.

Here’s a general format to declare a reference:

    dataType &referenceName = existingVariable;

You can use the reference just like you’d use the original variable.
When you change the value of the reference, the value of the original variable also changes, because they both share the same memory location.

*/

#include <iostream>

// Fucntion parameters
void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    int num = 10;
    int &ref = num;

    std::cout << ref << "\n";

    int x = 5, y = 10;
    std::cout << "Before Swap: x = " << x << " y = " << y << std::endl; // Outputs 5 10

    swap(x, y);
    std::cout << "After Swap: x = " << x << " y = " << y << std::endl; // Outputs 10 5

    return 0;
}