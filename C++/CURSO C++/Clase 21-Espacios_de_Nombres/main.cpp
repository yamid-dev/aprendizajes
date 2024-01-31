#include <iostream>

//Este es un espacio de nombre
namespace ciudad
{
    int calle;
}
namespace pueblito
{
    int calle = 10;
}

//Aqui defino que espacio de nombre utilizaré en el programa
using namespace ciudad;
int main()
{   
    calle = 12; //Aqui le doy valor a calle de ciudad
    std::cout << pueblito::calle << std::endl; //Aqui imprimo calle de pueblito
    std::cout << calle << std::endl; //Aqui imprimo la calle de ciudad
    std::cin.get();
    return 0;
}