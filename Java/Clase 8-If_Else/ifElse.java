public class ifElse {
    public static void main(String[] args) {
        int totalEpisodes = 1;

        if (totalEpisodes >1){
            System.out.println("Es una serie");
        }else if (totalEpisodes == 1){
            System.out.println("Es una pelicula");
        }else{
            System.out.println("Debe tener al menos un episodio");
        }
    }
}
