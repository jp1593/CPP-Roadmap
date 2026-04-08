/***  
Static Polymorphism: 
Type of polymorfism that resolves the types and methods calls at compile
time instead of doing it in runtime. 

Achieve with function overloading and templates in C++. 

***/

/*
Function overloading: 

Way to create multiple functions with the same name but different parameteres. 

Compiler determine the correct function to call based on the amount and type of the parameters
*/

#include <iostream>
#include <string>

// void print(int i) {
//     std::cout << "Printing int: " << i << '\n';
// }

// void print(double d) {
//     std::cout << "Printing double: " << d << '\n';
// }

// void print(const char* s) {
//     std::cout << "Printing string: " << s << '\n';
// }

// void print(std::string word, int number){
//     std::cout << "Custom: " << word << ' ' <<  number << '\n'; 
// }

// int main() {
//     print(5);          // Calls print(int i)
//     print(3.14);       // Calls print(double d)
//     print("Hello");    // Calls print(const char* s)
//     print("Hello customized", 20); 

//     return 0;
// }

/* 
Templates: 

Allows to create generic functions or classes. 

The code is generated at a compile time, avoiding overhead of runtime 
polymorphism. 

*/
template<typename T>
void print(const T& value) {
    std::cout << "Printing value: " << value << '\n';
}

template<typename C> 
C myMax( C x, C y){
    ret
}


int main() {
    print(42);           // int
    print(3.14159);      // double
    print("Hello");      // const char*
    print(true); 

}