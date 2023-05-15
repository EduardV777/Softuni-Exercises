import java.util.Scanner;

public class BasketballEquipment {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int yearlyFee = Integer.parseInt(input.nextLine());

        //prices
        double shoesPrice = yearlyFee - yearlyFee * 0.4;
        double jerseyPrice = shoesPrice - shoesPrice * 0.2;
        double ballPrice = jerseyPrice / 4;
        double accessoriesPrice = ballPrice / 5;

        double expenses = yearlyFee + shoesPrice + jerseyPrice + ballPrice + accessoriesPrice;

        System.out.println(expenses);
    }
}
