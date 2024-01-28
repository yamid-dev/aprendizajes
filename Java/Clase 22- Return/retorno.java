public class retorno {
    public static void main(String[] args){
        String[] titleArray = new String[]{"La naranja mecanica","Buscando a Nemo","Mision Imposible","Star Wars","Troya","Yo Robot","Ip Man"};
        String title = play(titleArray, 10);
        System.out.println("");
        pause(title);
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

    public static void pause(String title){
        if (title.isEmpty()){
            System.out.println("No movie playing");
        }else{
            System.out.println("Movie paused " + title);
        }
    }
}
