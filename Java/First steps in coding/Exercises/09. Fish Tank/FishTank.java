import java.util.Scanner;

public class FishTank {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int lengthCm = Integer.parseInt(input.nextLine());
        int widthCm = Integer.parseInt(input.nextLine());
        int heightCm = Integer.parseInt(input.nextLine());
        double spaceTakenPct = Double.parseDouble(input.nextLine());

        double waterSpace = lengthCm * widthCm * heightCm;
        waterSpace -= waterSpace * (spaceTakenPct / 100);
        waterSpace /= 1000;

        System.out.println(waterSpace);
    }
}