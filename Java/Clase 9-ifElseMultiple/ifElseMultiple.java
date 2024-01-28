public class ifElseMultiple {
    public static void main(String[] args) {
        int totalEpisodes = 12;
        int totalSeason = 2;

        if (totalEpisodes >1 || totalSeason > 1) {
            if (totalEpisodes <= 10){
                System.out.println("Es una miniserie");
            }else{
                System.out.println("Es una serie");
            }

        if (totalEpisodes > 1 && totalEpisodes <=10){
            System.out.println("Es una miniserie");
        }else if (totalEpisodes > 10){
            System.out.println("Es una serie");
        } else if (totalEpisodes == 1){
            System.out.println("Es una pelicula");
        }else{
            System.out.println("Debe tener al menos un episodio");
        }
    }
}
}  
   