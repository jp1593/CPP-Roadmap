// A lambda function, or simply “lambda”, is an anonymous (unnamed) function that is defined in place, within your source code, and with a concise syntax.
// at being a in line functions, this are simple are is unsual to call them a lot of times.
/*Sintaxis:

    [capture-list](parameters) -> return_type {
        // function body
    };

    Parameters:
   - capture-list: A list of variables from the surrounding scope that the lambda function can access.
   - parameters: The list of input parameters, just like in a regular function. Optional.
   - return_type: The type of the value that the lambda function will return. This part is optional, and the compiler can deduce it in many cases.
   - function body: The code that defines the operation of the lambda function.

    One or the benefits that it has that make them more powerfull than normal functions is the posibility to get variables out of its scope (capture-list)

*/

#include <iostream>
// Lambda Hello WorldLambda function with no capture, parameters, or return type.
auto printHello = []()
{
    std::cout << "Hello, World!" << std::endl;
};

// Lambda function with parameters
auto add = [](int a, int b)
{
    return a + b;
};
int result = add(3, 4);

int main()
{
    printHello();
    std::cout << result << "\n";

    // Lambda function with capture-by-value.
    int multiplier = 3;
    auto times = [multiplier](int a)
    {
        return a * multiplier;
    };
    int value = times(5); // result = 15
    std::cout << value << "\n";

    // Lambda function with capture - by - reference.

    int expiresInDays = 45;
    auto updateDays = [&expiresInDays](int newDays)
    {
        expiresInDays = newDays;
    };
    updateDays(30); // expiresInDays = 30
    std::cout << expiresInDays << "\n";

    return 0;
}