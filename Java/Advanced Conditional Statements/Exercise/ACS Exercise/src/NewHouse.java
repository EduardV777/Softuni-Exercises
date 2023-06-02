import java.util.Scanner;

public class NewHouse {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String typeFlowers = input.nextLine(); //"Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"
        int amount = Integer.parseInt(input.nextLine());
        int budget = Integer.parseInt(input.nextLine());

        double total = 0;

        //prices
        double roses = 5, dahlias = 3.80, tulips = 2.80, narcissus = 3, gladiolus = 2.50;

        switch(typeFlowers){
            case "Roses":
                total = roses * amount;

                if(amount > 80){
                    total -= total * 0.1;
                }
                break;
            case "Dahlias":
                total = dahlias * amount;

                if(amount > 90){
                    total -= total* 0.15;
                }
                break;
            case "Tulips":
                total = tulips * amount;

                if(amount > 80){
                    total -= total * 0.15;
                }
                break;
            case "Narcissus":
                total = narcissus * amount;

                if(amount < 120){
                    total += total * 0.15;
                }
                break;
            case "Gladiolus":
                total = gladiolus * amount;

                if(amount < 80){
                    total += total * 0.2;
                }
                break;
        }

        if(total <= budget){
            System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left.", amount, typeFlowers, (double)budget - total);
        }else {
            System.out.printf("Not enough money, you need %.2f leva more.", total - budget);
        }
    }
}
