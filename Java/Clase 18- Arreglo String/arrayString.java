public class arrayString {
      public static void main(String[] args){
        String[] movieTitleArray = new String[]{"Up","Titanic","Aladdin","Pepe el toro","Avengers","Matrix"};
        for (String title : movieTitleArray){
            if (!title.contains("e")){
                System.out.println(title);
            } 
        }
    }  
}
