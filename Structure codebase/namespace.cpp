/* Namespaces
This ones allow to name something defined by the programmer and use it into the code with the exception that namespaces has to be named different.

Provides a solution of name conflicts on larger projects.

Namespaces allows for identically named entities as long as the namespaces are different

To access to the thing that have been defined:

    namespace::(variable to access)
*/

#include <iostream>

using namespace std; // <--- Bad practice because it has a lot of entities on it that can have problems on namespaces own definitions, instead use: 
using std::cout; 
using std::string;


namespace firstnum{
    int num = 5; 
    string name = "hello";
}

namespace secondnum{ 
    int num = 2; 
}

int main(){

    cout << firstnum::num << std::endl; 
    cout << firstnum::name << std::endl;
    cout << secondnum::num; 

    return 0;

}