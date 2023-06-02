import java.util.Scanner;

public class SummerOutfit {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int deg = Integer.parseInt(input.nextLine());
        String timeOfDay= input.nextLine();

        String outfit = "", shoes = "";

        switch(timeOfDay){
            case "Morning":
                if(deg >= 10 && deg <= 18){
                    outfit = "Sweatshirt";
                    shoes = "Sneakers";
                }else if (deg > 18 && deg <= 24){
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }else if(deg >= 25){
                    outfit = "T-Shirt";
                    shoes = "Sandals";
                }
                break;
            case "Afternoon":
                if(deg >= 10 && deg <= 18){
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }else if (deg > 18 && deg <= 24){
                    outfit = "T-Shirt";
                    shoes = "Sandals";
                }else if(deg >= 25){
                    outfit = "Swim Suit";
                    shoes = "Barefoot";
                }
                break;
            case "Evening":
                if(deg >= 10 && deg <= 18){
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }else if (deg > 18 && deg <= 24){
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }else if(deg >= 25){
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }
                break;
        }

        System.out.printf("It's %d degrees, get your %s and %s.", deg, outfit, shoes);
    }
}
