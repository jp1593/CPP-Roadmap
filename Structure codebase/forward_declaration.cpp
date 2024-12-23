/*
Forward Declaration:
Way for declaring symbols, classes, functions or variables before being define on the code. Helps the compiler to identify the size of it.

*Usefull when having cyclic dependencies or for reducing compilation time (avoiding header inclusions on the src file)

*/

#include <iostream>
class ClassA; //<-- Forward declaration

// Is possible to use the pointers or references to the class without being defined.
void func(ClassA &obj);

class ClassB
{
public:
    void fwd(ClassA &obj);
};

int add(int a, int b); //<-- Forward declaration 

int main()
{
    int result = add(2, 3);
    // std::cout << result;

    return 0;
}