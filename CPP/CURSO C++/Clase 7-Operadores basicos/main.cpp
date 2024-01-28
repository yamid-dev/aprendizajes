#include <iostream>
#include <conio.h>
using namespace std;

int numero=12;
int numero2=10.0;

int suma;
int resta;
int mult;
int division;
int mode;
int operacion;

int main()
{
    //operadores basicos
    suma = numero + numero2;
    resta = numero - numero2;
    mult = numero * numero2;
    division = numero / numero2; 
    mode= numero % numero2;
    cout << "SUMA: " << suma << "\n" << "RESTA: " << resta << "\n" << "MULTIPLICACION: " << mult << "\n" << "DIVISION: " << division << "\n" << "MOD: "<< mode << "\n" << endl;
   

    //operadores de asignación
    operacion = 12;
    operacion += 13;
    operacion -= 3;
    operacion *=2;
    cout << operacion << endl;

    getch();
    return(0);
}