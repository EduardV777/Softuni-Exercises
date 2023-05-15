import java.util.Scanner;

public class Repainting {
    public static void main(String[] args) {

        //prices
        double safetyNylonPrice = 1.50;
        double paintPrice = 14.50;
        double paintThinnerPrice = 5.00;
        double workersPricePerHour = 0; //equals 30% of the sum of all materials
        double bagsPrice = 0.40;

        Scanner input = new Scanner(System.in);

        int nylonSqM = Integer.parseInt(input.nextLine());
        int paintL = Integer.parseInt(input.nextLine());
        int thinnerL = Integer.parseInt(input.nextLine());
        int jobHours = Integer.parseInt(input.nextLine());

        double expenses = ((double)(nylonSqM + 2) * safetyNylonPrice) + (((double)paintL + paintL * 0.1) * paintPrice) + ((double)thinnerL * paintThinnerPrice) + bagsPrice;
        workersPricePerHour = expenses * 0.3;
        expenses += workersPricePerHour * jobHours;

        System.out.println(expenses);
    }
}
