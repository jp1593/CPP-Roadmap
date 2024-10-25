#include <iostream>

int main (){
    // And & that takes two numbers, compares them bit by bit, and returns a new number where each bit is set (1) if the corresponding bits in both input numbers are set (1); otherwise, the bit is unset (0).
    int AND = 6 & 3; 
    std::cout << AND << "\n"; 

    // OR |  takes two numbers, compares them bit by bit, and returns a new number where each bit is set (2) if at least one of the corresponding bits in either input number is set (1); otherwise, the bit is unset (0).
    int OR = 6 | 3; 
    std::cout << OR << "\n";

    //XOR ^takes two numbers, compares them bit by bit, and returns a new number where each bit is set (1) if the corresponding bits in the input numbers are different; otherwise, the bit is unset (0).
    int XOR = 5 ^ 3; 
    std::cout << XOR << "\n"; 

    //NOT  takes two numbers, compares them bit by bit, and returns a new number where each bit is set (1) if the corresponding bits in the input numbers are different; otherwise, the bit is unset (0).
    int NOT = ~3; 
    std::cout << NOT << "\n"; 
    //Explanation of why NOT 3 returns -4 as result:
    // 1.  When you apply the NOT operator to 0000 0011, the result is: 1111 1100
    // 2. Interpreting the Result:
    // The result 1111 1100 is in two's complement format (the standard way of representing negative numbers in binary).
    // To find the decimal value of this binary number, you can convert it back to decimal:
    //     The leftmost bit is the sign bit (1 indicates a negative number).
    //     To convert from two's complement, you invert the bits and add 1:
    //         Invert 1111 1100 → 0000 0011
    //         Add 1 → 0000 0100 (which is 4 in decimal)
    //     Then ass the original binary was negative change the 4 to negative. 


    // Bitwise left shift operation (<<) is a binary operation that takes two numbers, a value and a shift amount, and returns a new number by shifting the bits of the value to the left by the specified shift amount. The vacated bits are filled with zeros. 
    int LEFTS = 5 << 3; 
    std::cout << LEFTS<< "\n"; 
    
    // Bitwise right shift operation (>>) is a binary operation that takes two numbers, a value and a shift amount, and returns a new number by shifting the bits of the value to the right by the specified shift amount. The vacated bits are filled with zeros or sign bit depending on the input value being signed or unsigned.
    int RIGHTS = 5 >> 2; 
    std::cout << RIGHTS<< "\n";
    return 0; 


}