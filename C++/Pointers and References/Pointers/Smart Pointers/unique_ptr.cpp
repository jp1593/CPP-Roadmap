/* Unique Pointer
std::unique_ptr is a smart pointer provided by the C++ Standard Library. It is a template class that is used for managing single objects or arrays, works with the concept
unique ownership. This ownership can be transferred or moved, but it cannot be shared or copied.
*/

#include <iostream>
#include <memory>

int main() {
    std::unique_ptr<int> p1(new int(5)); // Initialize with pointer to a new integer
    std::unique_ptr<int> p2 = std::make_unique<int>(10); // Preferred method (C++14 onwards)

    std::cout << *p1 << ", " << *p2 << std::endl;

    // Transformed ownership
        // std::unique_ptr<int> p2 = std::move(p1); // Ownership is transferred from p1 to p2
    return 0;
}