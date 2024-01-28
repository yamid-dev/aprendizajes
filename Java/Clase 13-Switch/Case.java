public class Case {
    public static void main(String[] args){
        int dayOfweek = 7;
        if (dayOfweek == 1) {
            System.out.println("Es lunes de comedia");
        }else if (dayOfweek == 2){
            System.out.println("Martes de  drama");
        }else if (dayOfweek == 3){
            System.out.println("Miercoles de accion");
        }else if (dayOfweek == 4){
            System.out.println("Jueves de animados");
        }else if (dayOfweek == 5){
            System.out.println("Viernes de animados");
        }else if (dayOfweek == 6){
            System.out.println("Sabados de documentales");
        }else if (dayOfweek == 7){
            System.out.println("Doomingo de comodín");
        }else{
            System.out.println("¿En que dia vives?");
        }

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
                break;
        }
    }
}
