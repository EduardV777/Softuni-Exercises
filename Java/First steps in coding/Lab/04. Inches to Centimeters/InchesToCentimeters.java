import java.util.Scanner;

public class InchesToCentimeters {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double inches = Double.parseDouble(input.nextLine());
        double cm = inches * 2.54;

        System.out.println(cm);
    }
}
