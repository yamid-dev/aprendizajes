#include <iostream>

using namespace std;

struct miestructura
{
    int a;
}miEstructura,*puntero;

int main()
{
    miEstructura.a = 12;
    puntero = &miEstructura;   
    
    cout << puntero << endl;
    cout << &miEstructura.a << endl;
    cout << miEstructura.a << endl;
    cout << puntero->a << endl;

    cin.get();
    return 0;
}