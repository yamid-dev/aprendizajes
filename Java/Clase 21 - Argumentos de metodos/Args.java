public class Args {
    public static void main(String[] args){
        String[] titleArray = new String[]{"La naranja mecanica","Buscando a Nemo","Mision Imposible","Star Wars","Troya","Yo Robot","Ip Man"};
        play(titleArray, 10);
        System.out.println("");
        pause();
    }
    public static void play(String[] listaDePelicula, int index){
        if (index < listaDePelicula.length){
            String title = listaDePelicula[index];
            for (int i = 0; i < 10; i++) {
                System.out.println("Playing movie "+title);
            }
        }else{
            System.out.println("Index is too big");
        }
        
    }

    public static void pause(){
        System.out.println("Movie paused");
    }
}
