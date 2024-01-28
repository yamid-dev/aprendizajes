#include <iostream>

using namespace std;

int main()
{   
    struct Hogar
    {
        int numeroDireccion;
        int numerotel;

        //esta es una funcion constructura de la estructura Hogar
        Hogar(){
            numeroDireccion = 0;
            numerotel = 2;
        }
        //esta es una funcion que hace algo
        int VerDir(){
            return numeroDireccion;
        }
        int GuardaDir (int a){
            numeroDireccion = a;
        }
    }Fernandez, Gonzales, Perez;
    
    Fernandez.numerotel = 1034;
    Fernandez.numeroDireccion = 324;

    Gonzales.numerotel = 1034;
    Gonzales.numeroDireccion = 324;

    Perez.GuardaDir(156);
    cout << Gonzales.numerotel << endl;
    cout << Perez.numerotel << endl;
    cout << Perez.VerDir() << endl;
    cin.get();
    return 0;
}