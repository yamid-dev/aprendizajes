public class experimento {
    public static void main(String[] args) {

        //Ejercicio 1 Cubo Rectangular
        int largo = 15;
        int ancho = 23;
        int alto = 12;

        int volumen = largo * ancho * alto;

        System.out.println(String.format("El volumen de el cubo rectangular es de %d",volumen));

        //Ejercicio 2 Energia cinetica

        int masa = 12;
        int velocidad = 3;

        double eneregiaCinetica = 0.5 * masa * Math.pow(velocidad,2);

        System.out.println(String.format("La eneregia cinetica es %.2f", eneregiaCinetica));


        //Ejercicio 3

        //a Para una "R" usamos una variable tipo char
        //b para eso usamos una variable tipo long
        //c Una variable tipo float
        //d Una de tipo boolean
        //e Una tipo int
        //f Una tipo string
        //g Una tipo double


        //Ejercicio 4

        double sesentaClics = 0.30;
        double cienClics = 0.25;
        double veinteClics = 0.80;
        double iva = 0.16;
        double promedioTotal = ((sesentaClics * 60) + (cienClics * 100) + (veinteClics * 20))/180;
        double promedioTotalIva = (iva * promedioTotal) + promedioTotal;

        System.out.println(String.format("Tu total es de $%.2f y el total + IVA es $%.2f",promedioTotal,promedioTotalIva));


    }
}