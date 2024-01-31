#include <iostream>
using namespace std;

int main()
{
    // Esto es un arreglo o lista
    char c[4];
    c[0] = 'H';
    c[1] = 'o';
    c[2] = 'l';
    c[3] = 'a';

    //Esto es un bucle for
    for (int i=0; i<4; i++)
    {
        cout << c[i];
    }
    cout << endl;
    cin.get();
    return 0;
}