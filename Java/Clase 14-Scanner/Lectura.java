import java.util.Scanner;
public class Lectura {
    public static void main(String[] args){
            System.out.println("¿QUÉ DIA DE LA SEMANA ES (LUNES = 1 - DOMINGO = 7)");
            Scanner scanner = new Scanner(System.in);
            int dayOfweek = scanner.nextInt();
            String myString = scanner.next();
            switch (dayOfweek){
                case 1:
                    System.out.println("Es lunes de comedia");
                    break;
                case 2:
                    System.out.println("Es Martes de drama");
                    break;
                case 3:
                    System.out.println("Miercoles de accion");
                    break;
                case 4:
                    System.out.println("Jueves de animados");
                    break;
                case 5:
                    System.out.println("Viernes de terror");
                    break;
                case 6:
                    System.out.println("Sábado de animados");
                    break;
                case 7:
                    System.out.println("Domingo de comodín");
                    break;
                default:
                    System.out.println("¿En que dia vives?");
            }
    }
}

/*import java.util.Scanner;

public class LeerEntradaUsuario {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese su nombre:");
        String nombre = scanner.nextLine();
        System.out.println("Hola, " + nombre + "!");
        scanner.close();
    }
}
 */
