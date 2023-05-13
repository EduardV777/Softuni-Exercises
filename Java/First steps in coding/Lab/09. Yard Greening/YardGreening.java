import java.text.DecimalFormat;
import java.util.Scanner;

public class YardGreening {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double sqMeters = Double.parseDouble(input.nextLine());
        double pricePerMeter = 7.61;
        double sale = 0.18;

        double total = sqMeters * pricePerMeter;
        double discount = total * sale;

        //take away sale from total
        total -= discount;

        String formattedTotal = formatNumber("###.##", total);
        String formattedDiscount = formatNumber("###.##", discount);

        System.out.printf("The final price is: %s lv.%n", formattedTotal);
        System.out.printf("The discount: %s lv.", formattedDiscount);
    }

    public static String formatNumber(String pattern, double val){
        DecimalFormat formatter = new DecimalFormat(pattern);
        String formattedVal = formatter.format(val);
        return formattedVal;
    }
}
