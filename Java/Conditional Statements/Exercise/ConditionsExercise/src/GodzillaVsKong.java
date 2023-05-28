import java.util.Scanner;

public class GodzillaVsKong {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double budget = Double.parseDouble(input.nextLine());
        int extras = Integer.parseInt(input.nextLine());
        double clothesPricePerExtra = Double.parseDouble(input.nextLine());

        double movieDecorPrice = budget * 0.1;

        if(extras > 150){
            clothesPricePerExtra -= clothesPricePerExtra * 0.10;
        }

        double totalExpenses = (extras * clothesPricePerExtra) + movieDecorPrice;

        if(totalExpenses > budget){
            System.out.printf("Not enough money!\nWingard needs %.2f leva more.", totalExpenses - budget);
        }else {
            System.out.printf("Action!\nWingard starts filming with %.2f leva left.", budget - totalExpenses);
        }
    }
}
