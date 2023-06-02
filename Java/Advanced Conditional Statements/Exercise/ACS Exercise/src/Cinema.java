import java.util.Scanner;

public class Cinema {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String projectionType = input.nextLine();
        int r = Integer.parseInt(input.nextLine());
        int c = Integer.parseInt(input.nextLine());

        double earnings = 0;


        switch(projectionType){
            case "Normal":
                earnings = 7.50 * (r * c);
                break;
            case "Premiere":
                earnings = 12.00 * (r * c);
                break;
            case "Discount":
                earnings = 5 * (r * c);
                break;
        }

        System.out.printf("%.2f", earnings);
    }
}
