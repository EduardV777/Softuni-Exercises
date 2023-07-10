import java.util.Scanner;

public class Journey {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double budget = Double.parseDouble(input.nextLine()), expenses = 0;
        String season = input.nextLine(), dest = "", restType = "";

        if(budget <= 100){
            //somewhere in Bulgaria
            dest = "Bulgaria";
            switch(season){
                case "summer":
                    restType = "Camp";
                    expenses = budget * 0.3;
                    break;
                case "winter":
                    restType = "Hotel";
                    expenses = budget * 0.7;
                    break;
            }
        }else if(budget <= 1000){
            dest = "Balkans";
            switch(season){
                case "summer":
                    restType = "Camp";
                    expenses = budget * 0.4;
                    break;
                case "winter":
                    restType = "Hotel";
                    expenses = budget * 0.8;
                    break;
            }
        }else {
            dest = "Europe";
            expenses = budget * 0.9;
            restType = "Hotel";
        }

        System.out.printf("Somewhere in %s\n%s - %.2f", dest, restType, expenses);
    }
}
