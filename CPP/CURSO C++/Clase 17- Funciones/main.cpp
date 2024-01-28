
#include <iostream>
int num1=0;
int num2=3;

int suma;

using namespace std;

//funcion de valor nulo
void funcion()
{
   cout << "Función sin valor de retorno " << endl;  
}

//fucion para sumar dos numeros
int sumar(int a, int b)
{
    return (a) + (b);
}

//funcion principal
int main()
{   
    suma= sumar(num1, num2);
    cout << suma << endl;
    funcion();
    cin.get();
    return 0;
}