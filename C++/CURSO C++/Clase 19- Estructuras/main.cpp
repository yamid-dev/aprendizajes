#include <iostream>

using namespace std;

int main()
{   
    //esta es una estructura llamada personaje
    struct personaje
    {
        int edad;
        int tel;
    }Santiago;
    Santiago.edad=18;
    Santiago.tel=3002001001;
    cout<< Santiago.edad << endl;
    
    cin.get();
    return 0;
}