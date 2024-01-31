#include <iostream>
using namespace std;

/*
Esto es un ejemplo de comentario
Esta es otra linea
Esta es otra
Esta también
.
..
.
ÚLTIMA LINEA.
*/

//Esto es un comentario

int main()
{
    char c;
    cout << "Escribe una letra" << endl;
    cin >> c;
    
    switch(c)
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            cout << "Es una vocal\n";
            break;
        default:
            cout << "Es una consonante\n" << endl;
    }
    system("PAUSE");
    return(0);
}