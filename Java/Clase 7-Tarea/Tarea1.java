public class Tarea1 {
    public static void main(String[] args){
        System.out.println("EJERCICIO 1: PRISMA RECTANGULAR");
        //V=Ab+Hc
        //Ab=lxl
        double largo = 15;
        double ancho = 23;
        double altura = 12;
        System.out.println(String.format("Largo: %.0f\nAncho: %.0f\nAltura: %.0f",largo,ancho,altura));
        System.out.println("Volumen= "+((15*23)*altura)+" m^3\n");
        
        System.out.println("EJERCICIO 2: FORMULA CINETICA\n");    
        double m=12;
        System.out.println(m);
        double v=Math.pow(3,2);
        System.out.println(v);
        double x=1/2f;
        System.out.println(x);
        double eC= x*m*v;
        System.out.println("EC= "+eC+" J");

        System.out.println("\nEJERCICIO 3: TIPOS DE VARIABLES PARA...\na. 'R': char\nb. 1495970192837664: long\nc. 12.5: float\nd. true: boolean\ne. 90: int\nf. ¡No tengo trono ni reina, ni nadie que me comprenda, pero sigo siendo el rey!: String\ng. 6.626070040: double"+"\n");    
       /* calcular costo promedio para 180 clics:
       60 clics= 0.30
       100 clicls = 0.25
       20 clics = 0.80
       El costo por clic promedio (CPC prom.), se divide el costo total de clics por la cantidad total de clics*/
       double totalSinIva=(60*0.30)+(100*0.25)+(20*0.80);
       double iva= totalSinIva*0.16;
       double totalConIva= totalSinIva+iva;
       double total= totalConIva/180;
       String cad = String.valueOf(total);
       cad= cad.substring(0, 4);
       total = Double.parseDouble(cad);
       System.out.println("Total sin iva: "+(totalSinIva)+"/ IVA: "+(iva)+"/ TOTAL:"+(iva+totalSinIva)+"\nCOSTO PROMEDIO POR CLICK: "+(total));
    }   
}
