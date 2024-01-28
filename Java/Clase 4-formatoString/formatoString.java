public class formatoString{
    public static void main(String[] args){
        int edad=25; //variable entera
        float altura= 1.70f; //variable de coma flotante
        double valorDePi=3.141597843485821; // variable de coma flotante para valores con muchos decimales
        long distanciaAlSol = 1234567890123456789L; //variable similar a la de tipo entero, pero para numeros mucho más grandes
        boolean IsDay = false;
        char miInicial='y';

        System.out.println(String.format("Mi edad es %d %d ", edad,distanciaAlSol));
        System.out.println("Mi altura es " + altura );
        System.out.println(String.format("Mi altura es %.3f",valorDePi));
    }
}