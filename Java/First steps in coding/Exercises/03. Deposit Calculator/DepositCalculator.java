import java.util.Scanner;
import java.text.DecimalFormat;

public class DepositCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double deposit = Double.parseDouble(input.nextLine());
        int period = Integer.parseInt(input.nextLine());
        double annualIR = Double.parseDouble(input.nextLine()) / 100;

        double sum = deposit + period * ((deposit * annualIR) / 12);

        System.out.println(FormatValue("###.##", sum));
    }

    public static String FormatValue(String pattern, double val){
        DecimalFormat formatter = new DecimalFormat(pattern);
        String formattedValue = formatter.format(val);
        return formattedValue;
    }
}
