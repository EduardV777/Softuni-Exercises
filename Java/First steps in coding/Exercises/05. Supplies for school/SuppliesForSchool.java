import java.util.Scanner;

public class SuppliesForSchool {
    public static void main(String[] args){
        //prices
        double pensPrice = 5.80;
        double markersPrice = 7.20;
        double cleaningSolutionPrice = 1.20;

        Scanner input = new Scanner(System.in);

        int penPackages = Integer.parseInt(input.nextLine());
        int markerPackages = Integer.parseInt(input.nextLine());
        int cleaningSolutionLitres = Integer.parseInt(input.nextLine());
        int discountRate = Integer.parseInt(input.nextLine());

        double total = penPackages * pensPrice + markerPackages * markersPrice + cleaningSolutionLitres * cleaningSolutionPrice;
        total -= total * ((double) discountRate / 100);

        System.out.println(total);
    }
}
