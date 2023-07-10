import java.util.Scanner;
public class CourierExpress {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double packageWeight = Double.parseDouble(input.nextLine());
        String serviceType = input.nextLine();
        int distanceKm = Integer.parseInt(input.nextLine());

        double transportCost = 0.00;

        switch(serviceType){
            case "standard":
                if(packageWeight < 1.00){
                    transportCost = 0.03;

                }else if(packageWeight < 10){
                    transportCost = 0.05;

                }else if(packageWeight < 40){
                    transportCost = 0.10;

                }else if(packageWeight < 90){
                    transportCost = 0.15;

                }else if(packageWeight < 150){
                    transportCost = 0.20;
                }

                transportCost = transportCost * distanceKm;
                break;

            case "express":
                if(packageWeight < 1.00){
                    transportCost = 0.03;
                    transportCost *= distanceKm;
                    transportCost += transportCost * 0.8 * packageWeight;

                }else if(packageWeight < 10){
                    transportCost = 0.05;
                    transportCost *= distanceKm;
                    transportCost += transportCost * 0.4 * packageWeight;

                }else if(packageWeight < 40){
                    transportCost = 0.10;
                    transportCost *= distanceKm;
                    transportCost += transportCost * 0.05 * packageWeight;

                }else if(packageWeight < 90){
                    transportCost = 0.15;
                    transportCost *= distanceKm;
                    transportCost += transportCost * 0.02 * packageWeight;

                }else if(packageWeight < 150){
                    transportCost = 0.20;
                    transportCost *= distanceKm;
                    transportCost += transportCost * 0.01 * packageWeight;
                }
                break;
        }

        System.out.printf("The delivery of your shipment with weight of %.3f kg. would cost %.2f lv.", packageWeight, transportCost);
    }
}
