#include <iostream>

using namespace std;

int array[5];
int *p;

int main()
{   
    p = array;
    cout << "Dirección array[0]"<< &array << endl;
    cout << "puntero" << p << endl;
    cin.get();
    return 0;
}