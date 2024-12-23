/* 
Scope = Accesibility and visibility of variables, functions, classes and other identities.
*/

#include <iostream>
// Global: Identifiers declared outside functions or classes (accessible for any part of the program / Lifetime: Entire duration of program)
// [Can be hidden by a local identifier with the same name]

int global = 7;

//Local: Identifiers declared on a function or block (accessible only from the function or block they have been declared / Lifetime: Execution of function or block.)
int local(){
    int localvar = 16; 
    return localvar;
}

int main()
{
    std::cout << "Global variable: " << global << std::endl;
    std::cout << local;
}
