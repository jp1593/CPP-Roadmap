#include <iostream>

using namespace std;

int main()
{
    /* For Loop
    Used when the number of iterations is known, it is composed by the following structure:
    for (initialization; condition; increment/decrement) {
        // block of code to execute
    }
    */
    cout << "FOR LOOP \n";
    for (int i = 0; i < 5; i++)
    {
        cout << "Iteration: " << i << std::endl;
    }

    /* While
    Accomplished or iterated everytime a condition is true
    while (condition) {
        // block of code to execute
    }
    */
    cout << "\nWHILE LOOP \n";
    int j = 0;
    while (j < 5)
    {
        std::cout << "Iteration: " << j << std::endl;
        j++;
    }

    /* Do-While
        Accomplished or iterated everytime a condition is true with the DIFERRENCE that it execute at least once even if the condition is false
        - Similar to While
        do {
         // block of code to execute
        } while (condition);while (condition) {
        */
    cout << "\nDO-WHILE\n";
    int k = 0;
    do
    {
        cout << "Iteration: " << k << endl;
        k++;
    } while (k < 5);

    return 0;
}