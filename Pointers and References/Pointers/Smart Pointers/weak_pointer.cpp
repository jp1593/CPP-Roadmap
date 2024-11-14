/* Weak Pointer
A weak_ptr is a type of smart pointer in C++ that adds a level of indirection and safety to a raw pointer.

It is mainly used to break reference cycles in cases where two objects have shared pointers to each other or
an invalid reference make by a shared_ptr

To use a weak_ptr, you must convert it to a shared_ptr using the lock() function, which tries to create a new shared_ptr 
that shares ownership of the object.

*/

#include <iostream>
#include <memory>

class MyClass {
public:
    void DoSomething() {
        std::cout << "Doing something...\n";
    }
};

int main() {
    std::weak_ptr<MyClass> weak;

    {
        std::shared_ptr<MyClass> shared = std::make_shared<MyClass>();
        weak = shared;

        if(auto sharedFromWeak = weak.lock()) {
            sharedFromWeak->DoSomething(); // Safely use the object
            std::cout << "Shared uses count: " << sharedFromWeak.use_count() << '\n'; // 2
        }
    }

    // shared goes out of scope and the MyClass object is destroyed

    if(auto sharedFromWeak = weak.lock()) {
        // This block will not be executed because the object is destroyed
    }
    else {
        std::cout << "Object has been destroyed\n";
    }

    return 0;
}