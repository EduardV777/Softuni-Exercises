import java.util.Scanner;

public class USDtoBGN {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        double usd = Double.parseDouble(input.nextLine());
        double rate = 1.79549;
        double bgn = usd * rate;

        System.out.println(bgn);
    }
}