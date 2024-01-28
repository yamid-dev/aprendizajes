public class cicloDoWhile {
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
        int i = 15;
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
        System.out.println("===============================================================");
        for (int j = 0; j <= duration; j++){
            if (j < 3){
                System.out.println("Reproduciendo intro, segundo = " + j);
            } else if (j<7){
                System.out.println("Reproduciendo pelicula, segundo = " + j);
            } else {
                System.out.println("Reproduciendo creditos, segundo = " + j);
            }
            i++;
        }
        System.out.println("===============================================================");

        int k = 0;
        do{
            if (k<3){
                System.out.println("Reproduciendo into, segundo = "+k);
            }else if (k < 7){
                System.out.println("Reproduciendo película, segundo = "+k);
            }else{
                System.out.println("Reproduciendo créditos, segundo = "+k);
            }
            
        } while (k<=duration);
    }
}
