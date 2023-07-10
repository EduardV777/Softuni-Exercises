import java.util.Scanner;

public class FishingBoat {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int budget = Integer.parseInt(input.nextLine());
        String season = input.nextLine();
        int fishers = Integer.parseInt(input.nextLine());

        double boatRent = 0;

        switch(season){
            case "Spring":
                boatRent = 3000;

                if(fishers <= 6){
                    boatRent -= boatRent * 0.1;
                }else if(fishers >= 7 && fishers <= 11){
                    boatRent -= boatRent * 0.15;
                }else if(fishers >= 12){
                    boatRent -= boatRent * 0.25;
                }

                if(fishers % 2 == 0){
                    boatRent -= boatRent * 0.05;
                }
                break;
            case "Summer":
                boatRent = 4200;

                if(fishers <= 6){
                    boatRent -= boatRent * 0.1;
                }else if(fishers >= 7 && fishers <= 11){
                    boatRent -= boatRent * 0.15;
                }else if(fishers >= 12){
                    boatRent -= boatRent * 0.25;
                }

                if(fishers % 2 == 0){
                    boatRent -= boatRent * 0.05;
                }
                break;
            case "Autumn":
                boatRent = 4200;

                if(fishers <= 6){
                    boatRent -= boatRent * 0.1;
                }else if(fishers >= 7 && fishers <= 11){
                    boatRent -= boatRent * 0.15;
                }else if(fishers >= 12){
                    boatRent -= boatRent * 0.25;
                }

                break;
            case "Winter":
                boatRent = 2600;

                if(fishers <= 6){
                    boatRent -= boatRent * 0.1;
                }else if(fishers >= 7 && fishers <= 11){
                    boatRent -= boatRent * 0.15;
                }else if(fishers >= 12){
                    boatRent -= boatRent * 0.25;
                }

                if(fishers % 2 == 0){
                    boatRent -= boatRent * 0.05;
                }
        }

        if(boatRent <= budget){
            System.out.printf("Yes! You have %.2f leva left.", (double)budget - boatRent);
        }else {
            System.out.printf("Not enough money! You need %.2f leva.", boatRent - budget);
        }

    }
}
