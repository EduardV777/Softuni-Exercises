import java.util.Scanner;

public class DeerOfSanta {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int daysAway = Integer.parseInt(input.nextLine());
        int foodLeftKg = Integer.parseInt(input.nextLine());
        double foodForStag1 = Double.parseDouble(input.nextLine());
        double foodForStag2 = Double.parseDouble(input.nextLine());
        double foodForStag3 = Double.parseDouble(input.nextLine());

        double totalFoodRequired = (foodForStag1 + foodForStag2 + foodForStag3) * daysAway;

        if(foodLeftKg >= totalFoodRequired){
            System.out.printf("%.0f kilos of food left.", Math.floor(foodLeftKg - totalFoodRequired));
        }else {
            System.out.printf("%.0f more kilos of food are needed.", Math.ceil(totalFoodRequired - foodLeftKg));
        }
    }
}
