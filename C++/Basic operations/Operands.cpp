#include <iostream>

using namespace std;

int main () { 
    int a = 4;
    int b = 7; 
    int quotient = a / b;
    float fquotient = float(a) / float(b); 
    cout << "Int:" << quotient << "\n"; 
    cout << "Float:" << fquotient; 
    return 0; 
}