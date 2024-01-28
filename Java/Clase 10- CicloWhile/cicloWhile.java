public class cicloWhile {
    public static void main(String[] args) {
        int totalEpisodes = 1;

        if (totalEpisodes > 1 && totalEpisodes <=10){
            System.out.println("Es una miniserie");
        }else if (totalEpisodes > 10){
            System.out.println("Es una serie");
        } else if (totalEpisodes == 1){
            System.out.println("Es una pelicula");
        }else{
            System.out.println("Debe tener al menos un episodio");
        }
        int i = 0;
        int duration = 10;
        while(i <= duration){
            if (i < 3){
                System.out.println("Reproduciendo intro, segundo = " + i);
            } else if (i<7){
                System.out.println("Reproduciendo pelicula, segundo = " + i);
            } else {
                System.out.println("Reproduciendo creditos, segundo = " + i);
            }

            i++;
        }
    }
}
