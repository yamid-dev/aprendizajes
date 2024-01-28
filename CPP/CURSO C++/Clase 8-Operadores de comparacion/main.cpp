#include <iostream>
#include <conio.h>
using namespace std;
bool comprobador1;
bool comprobador2;
bool comprobador3;
bool comprobador4;

int numero1 = 12;
int numero2 = 0;

int main()
{
    comprobador1 = (numero1 == numero2);
    comprobador2 = (numero1 != numero2);
    comprobador3 = (numero1 > numero2); 
    comprobador4 = (numero1 < numero2);
    cout << comprobador1 << "\n" << comprobador2 << "\n" << comprobador3 << "\n" << comprobador4 <<  endl;
    getch();
    return(0);
}