import java.text.DecimalFormat;
import java.util.Scanner;
public class PetShop {
    public static void main(String[] args){
        double dogFood = 2.50;
        double catFood = 4.00;

        Scanner input = new Scanner(System.in);

        int dogFoodPackages = Integer.parseInt(input.nextLine());
        int catFoodPackages = Integer.parseInt(input.nextLine());
        double total = (dogFoodPackages * dogFood) + (catFoodPackages * catFood);

        String formattedTotal = formatNumber("###.#", total);
        System.out.printf("%s lv.", formattedTotal);
    }

    public static String formatNumber(String pattern, double val){
        DecimalFormat formatter = new DecimalFormat(pattern);
        String formattedNum = formatter.format(val);
        return formattedNum;
    }
}
