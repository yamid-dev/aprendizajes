import java.util.Scanner;
public class Tarea2{
    public static void main(String[] args){
        System.out.print("¿QUÉ EJERCICIO DESEAS PROBAR?:\n1. Ejercicio 1\n2. Ejercicio 2\n3. Ejercicio 3\n4. Ejercicio 4\n5. Ejercicio 5\n6. Ejercicio 6\n>>>");
        Scanner sc = new Scanner(System.in);
        int ejercicio = sc.nextInt();
        switch (ejercicio){
                    case 1:
                        System.out.println("=======================================\nEJERCICIO 1");
                        Scanner scanner = new Scanner (System.in);
                        System.out.print("Ingrese la cantidad de miligramos para la poción multijugos: ");
                        int miligramos = scanner.nextInt();
                        if (miligramos > 100){
                            System.out.println("¡Felicidades es una buena poción!");
                        }else{
                            System.out.println("La poción es mediocre, sangre sucia inmunda");
                        }
                        break;

                    case 2:
                        System.out.println("=======================================\nEJERCICIO 2");
                        Scanner x = new Scanner (System.in);
                        System.out.print("Ingrese la distancia del conductor en Km: ");
                        Double distanciaCondutor = Double.parseDouble(x.nextLine().replace(",","."));
                        System.out.print("Ingrese si el conductor está disponible (true, false): ");
                        boolean disponibilidad = x.nextBoolean();
                        if (distanciaCondutor <= 0.5 && disponibilidad == true){
                            System.out.println("Listo para el recorrido");
                        } else if (distanciaCondutor <= 0.5 && disponibilidad == !true){
                            System.out.println("Conductor cercano pero no disponible");
                        } else if (distanciaCondutor > 0.5 && disponibilidad == true){
                            System.out.println("Conductor disponible pero muy lejos, aplicará tarifas muy altas");
                        }else{
                            System.out.println("No hay conductores disponibles");
                        }
                        break;

                    case 3:
                        System.out.println("=======================================\nEJERCICIO 3");
                        Scanner y = new Scanner (System.in);
                        System.out.print("Ingrese un número n: ");
                        int n = y.nextInt();
                        int cont = 0;
                        int acum = 0;
                        System.out.println("================CICLO WHILE================");
                        while (cont < n){
                                    cont ++;
                                    acum +=cont;
                                    System.out.println("Iteracion "+cont+" = "+acum);
                        }
                        System.out.println("La suma de 1 hasta "+n+" es "+acum);
                        acum=0;
                        System.out.println("=================CICLO FOR===================");
                        for (int i=1; i<=n; i++){
                            acum+=(i);
                            System.out.println("Iteracion "+i+" = "+acum);
                        }
                        System.out.println("La suma de 1 hasta "+n+" es "+acum);
                        break;

                    case 4:
                        System.out.println("=======================================\nEJERCICIO 4");
                        System.out.println("¿CÓMO ESTÁ EL CLMA HOY?");
                        Scanner w=new Scanner (System.in);
                        System.out.print("Ingrese una opción: \n1 : Soleado\n2 : Nublado\n3 : Lluvioso\n4 : Tormentoso\n5 : Nevado\n Otro: Buscalo en Google\n\n>>>");
                        int opc = w.nextInt();
                        switch (opc){
                            case 1:
                                System.out.println("Soleado");
                                break;
                            case 2:
                                System.out.println("Nublado");
                                break;
                            case 3:
                                System.out.println("LLuvioso");
                                break;
                            case 4:
                                System.out.println("Tormentoso");
                                break;
                            case 5:
                                System.out.println("Nevado");
                                break;
                            default:
                                System.out.println("Pregúntale a Google");
                                break;
                        }
                        break;
                    case 5:
                        System.out.println("=======================================\nEJERCICIO 5");
                        String[] lista = new String[]{"Titanic","Bajo La Misma Estrella","Eterno Resplandor de una mente sin recuerdos","El Joker","La Mascara","La Momia"};
                        int may = 0;
                        int i=0;
                        int indice = 0;
                        String p="";
                        for (String elemento : lista){
                            i++;
                            int len= elemento.length();
                            if ( len > may) {
                                may = len;
                                p= elemento;
                                indice = i;
                            }
                        }
                        System.out.println(may+" letras: "+p+" ( indice "+indice+")");
                        break;
                    case 6:
                        System.out.println("=======================================\nEJERCICIO 6");
                        Scanner z = new Scanner(System.in);
                        System.out.println("Ingrese un número: ");
                        int numb = z.nextInt();
                        if (numb <= 0){
                            System.out.println("Inserta un número positivo");
                        } else{
                            for (int s = 0; s <= numb; s+=2) {
                                if (s == numb - 1 || s == numb){
                                    System.out.print(s);
                                } else{
                                    System.out.print(s+", ");
                                }
                            }
                        }
                        break;
                    default:
                    System.out.println("ERROR: Elegiste una opción que no existe");
                        break;
        }
    }
}