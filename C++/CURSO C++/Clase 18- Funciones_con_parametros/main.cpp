#include <iostream>

using namespace std;

void funcion(int num = 2); // Esta funcion tomará el valor de 2 como argumento, si no se le pasa ningun valor;

int main()
{   
    funcion();
    funcion(12); //Al llamar a esta funcion el argumento se transformará de 2 a 12
    cin.get();
    return 0;
}

void funcion (int num)
{
    cout << (num + 3) << endl;
}