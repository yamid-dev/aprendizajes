

// import java.util.Scanner;
// public class arrays {
//     public static void main(String[] args){
//         System.out.println("Escribe el numero de episodios que quisieras saber su duracion");
//         Scanner scanner = new Scanner(System.in);
//         int episodeIndex=scanner.nextInt();

//         int[] episodeDurationArray = new int[5];

//         episodeDurationArray[0] = 30;
//         episodeDurationArray[1] = 32;
//         episodeDurationArray[2] = 27;
//         episodeDurationArray[3] = 31;
//         episodeDurationArray[4] = 60;

//         int[] episodeDuration = episodeDurationArray[episodeIndex];
//         System.out.println("El episodio dura "+episodeDuration+" minutos");

//     }
// }

import java.util.Scanner;

public class arrays {
    public static void main(String[] args) {
        System.out.println("Escribe el número de episodios cuya duración quieres saber");
        Scanner scanner = new Scanner(System.in);
        int episodeIndex = scanner.nextInt();
        episodeIndex--;
        int[] episodeDurationArray = new int[5];

        episodeDurationArray[0] = 30;
        episodeDurationArray[1] = 32;
        episodeDurationArray[2] = 27;
        episodeDurationArray[3] = 31;
        episodeDurationArray[4] = 60;

        if (episodeIndex >=0 && episodeIndex < 5){
            int episodeDuration = episodeDurationArray[episodeIndex];
            System.out.println("El episodio dura " + episodeDuration + " minutos");
        } else{
            System.out.println("ERROR, la serie solo tiene 5 episodios");
        }
        
    }
}

