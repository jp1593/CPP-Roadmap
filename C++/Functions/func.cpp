#include <iostream>

//Format of functions: 
/*  
    return_type function_name(parameter list) {
        // function body
    }

*/ 

//Prototype function
int multiplyNumbers(int x, int y); // Declaration of function without body

int addNumbers(int a, int b) {
    int sum = a + b;
    return sum;
}

int main() {
    int num1 = 5, num2 = 10;
    int result = addNumbers(num1, num2); // Calling the function
    std::cout << "The sum is: " << result << std::endl;

    int a = 17, b = 28; 
    int prototype = multiplyNumbers(a, b); // Calling the function
    std::cout << "The product is: " << prototype << std::endl;

    return 0;
}

// Function definition - Prototype
int multiplyNumbers(int x, int y) {
    int product = x * y;
    return product;
}

