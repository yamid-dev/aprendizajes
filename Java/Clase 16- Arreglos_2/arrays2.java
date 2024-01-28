import java.util.Scanner;

public class arrays2 {
    public static void main(String[] args) {
        System.out.println("Escribe el número de episodios cuya duración quieres saber");
        Scanner scanner = new Scanner(System.in);
        int episodeIndex = scanner.nextInt();
        episodeIndex--;
        int[] episodeDurationArray = new int[]{30,32,27,31,60};
        int n = episodeDurationArray.length;

        if (episodeIndex >=0 && episodeIndex < n){
            int episodeDuration = episodeDurationArray[episodeIndex];
            System.out.println("El episodio dura " + episodeDuration + " minutos");
        } else{
            System.out.println("ERROR, la serie solo tiene " + n + " episodios");
        }
        
    }
}