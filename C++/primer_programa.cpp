#include <iostream>
#include <string>
#include <locale>
using namespace std;

int main()
{
    setlocale(LC_ALL, "");
    int a;
    int cont = -1;
    int edad;
    wstring nombre;
    wcout << L"Ingrese su nombre: ";
    getline(wcin, nombre);
    wcout << L"Ingrese su edad: ";
    wcin >> edad;
    wcout << L"Ingrese el año actual: ";
    wcin >> a;

    wcout << L"Hola " << nombre << L"\n" << L"Tu edad es " << edad << L"\n";

    for (int i = 0; i <= edad; i++) {
        cont++;
        if (i == edad) {
            wcout << L"Naciste en el año " << ((a - 1) - cont) << L"\n";
        } else {
            wcout << L"Cumpliste " << (edad - cont) << L" años de edad en " << ((a - 1) - cont) << L"\n";
        }
        if (cont == edad) {
            break;
        }
    }
    system("PAUSE");
    return 0;
}