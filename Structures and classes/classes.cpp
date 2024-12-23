/*

Classes:
User defined data structure in which each member has a private access by default

The members of the classes can only be accesed by the methods of the class
*/

#include <iostream>

class Student
{
    int id;
    int age;
    std::string name;
    std::string lastname;

public:
    void setData(int id, int age, std::string name, std::string lastname)
    {
        this->id = id;
        this->age = age;
        this->name = name;
        this->lastname = lastname;
    }

    void getData() {
        std::cout << "ID:" << id << "\nAge:" << age << "\nName:" << name << "\nLastName:" << lastname; 
    }
};

int main (){
    Student firststudent; 
    firststudent.setData(100, 21, "Alex", "Padilla");
    firststudent.getData();
    return 0;
}