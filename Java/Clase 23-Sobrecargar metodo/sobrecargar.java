import java.util.Random;
public class sobrecargar {
    public static void main(String[] args){
        String[] titleArray = new String[]{"La naranja mecanica","Buscando a Nemo","Mision Imposible","Star Wars","Troya","Yo Robot","Ip Man"};
        String title = play(titleArray, 3);
        String title2 = play(titleArray);
        System.out.println("");
        pause(title);
        System.out.println("");
        pause(title2);
    }

    public static String play(String[] listaDePelicula, int index){
        if (index < listaDePelicula.length){
            String title = listaDePelicula[index];
            for (int i = 0; i < 10; i++) {
                System.out.println("Playing movie "+title);
            }

            return title;
        }else{
            System.out.println("Index is too big");
            return "";
        }
    }
    
    //funciones con el mismo nombre pero diferentes metodos = sobrecargar
    public static String play(String[] listaDePelicula){
            Random random = new Random();
            int index = random.nextInt(listaDePelicula.length);
            String title = listaDePelicula[index];
            for (int i = 0; i < 10; i++) {
                System.out.println("Playing movie "+title);
            }
            return title;
    }
    
    public static void pause(String title){
        if (title.isEmpty()){
            System.out.println("No movie playing");
        }else{
            System.out.println("Movie paused " + title);
        }
    }
}