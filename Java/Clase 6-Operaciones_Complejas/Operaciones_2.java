public class Operaciones_2 {
    public static void main(String[] args){
        //rectangle
        int b=15;
        int a=8;

        //Area
        int rArea=b*a;

        //Perimeter
        int perimeter=(2*b)+(2*a);

        //Triangle
        b=5;
        a=3;

        //Area
        double tArea=b*a/2.0;

        //Circle
        int r=60;

        //Area
        double pi=Math.PI;
        double cArea = pi*Math.pow(r,2);

        System.out.println(cArea);

        //Hipotenuse
        double sumaCatetos =  Math.pow(a,2) + Math.pow(b,2);
        double area= Math.sqrt(sumaCatetos);
        
        System.out.println(area);
    }    
}