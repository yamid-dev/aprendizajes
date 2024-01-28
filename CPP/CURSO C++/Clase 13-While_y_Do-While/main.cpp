#include <iostream>
using namespace std;

int main()
{
    
    int i = 0;

    // Estructura del bucle while
    while (i <=5)
    {
        cout << i << endl;
        i++;
    }

    //Estructura  del bucle do while
    do
    {
        cout << i << endl;
        i++;
    } while (i <=5);
    cin.get();
    return 0;
}