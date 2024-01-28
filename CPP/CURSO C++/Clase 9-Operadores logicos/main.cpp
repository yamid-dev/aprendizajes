#include <iostream>
using namespace std;
bool comprobador1;
bool comprobador2;
bool comprobador3;


int num1, num2, num3, num4;

int main()
{
    num1 = 12;
    num2 = 20;
    num3 = 4;
    num4 = 13;

    comprobador1 = (num4 > num1 && num3 < num2);
    comprobador1 = (num4 > num1 || num3 < num2);
    comprobador3= !(num4 > num1);
    cout<< comprobador1 << "\n" << comprobador2 << "\n" << comprobador3 << endl;
    cin.get();
    return(0);
}