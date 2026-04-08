// Raw pointers in C++ are low-level constructs that directly hold a memory address.

#include <iostream>
int main()
{
    // New Operator (used to allocate memory on the heap) it keeps alive until you deallocated it.
    int *ptr = new int; // Dynamically allocates an int on the heap
    *ptr = 42;          // Assigns the value 42 to the allocated int

    // Delete Opeator (used to deallocate memory that has been allocated with NEW) after memory is deallocated, it’s available to be reallocated for other purposes.
    delete ptr; // Deallocates the memory assigned to ptr

    // The new[] and delete[] operators are used for allocating and deallocating memory for an array of objects.
    int n = 10;
    int *arr = new int[n]; // Dynamically allocates an array of 10 integers on the heap

    // Set some values in the array
    for (int i = 0; i < n; i++)
    {
        arr[i] = i;

        std::cout << *arr;
    }
    delete[] arr; // Deallocates the memory assigned to the array

    return 0;
}