#include <iostream>
using namespace std;

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