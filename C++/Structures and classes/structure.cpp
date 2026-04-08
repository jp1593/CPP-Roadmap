/*

Structure:
User-defined data types that envolves mulptiple variables in one place, with public access of them.

Each variable inside the structure is called a MEMBER

*/

#include <iostream>

struct Car
{
    std::string engine;
    int doors;
    std::string brand = "Renault";
    bool transmission;
};

int main()
{
    Car c1; //Object creation by struct

    //Members acces of the struct
    c1.engine = "2.5 L";
    c1.doors = 4; 
    // c1.brand = "Ferrari"; 
    c1.transmission = 1;

    std::cout << "Car: " << c1.brand;
}