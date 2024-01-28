#include <iostream>
using namespace std;
int num1 = 5;
int num2 = 10;

int main()
{
    if (num1<num2){
        cout << "Es menor" << endl;
    }else if (num1==num2){
        cout << "Valen lo mismo" << endl;
    }else{
        cout << "no es menor" << endl;
    }
    cin.get();
    return(0);
}