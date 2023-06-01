import java.util.Scanner;

public class TradeCommissions {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String city = input.nextLine();
        double amountSales = Double.parseDouble(input.nextLine());
        double commission = 0;
        boolean valid = true;

        switch(city){
            case "Sofia":
                if(amountSales >= 0 && amountSales <= 500){
                    commission = amountSales * 0.05;
                } else if (amountSales > 500 && amountSales <= 1000){
                    commission = amountSales * 0.07;
                }else if (amountSales > 1000 && amountSales <= 10000){
                    commission = amountSales * 0.08;
                }else if(amountSales > 10000){
                    commission = amountSales * 0.12;
                }else {
                    valid = false;
                }
                break;
            case "Plovdiv":
                if(amountSales >= 0 && amountSales <= 500){
                    commission = amountSales * 0.055;
                } else if (amountSales > 500 && amountSales <= 1000){
                    commission = amountSales * 0.08;
                }else if (amountSales > 1000 && amountSales <= 10000){
                    commission = amountSales * 0.12;
                }else if(amountSales > 10000){
                    commission = amountSales * 0.145;
                }else {
                    valid = false;
                }
                break;
            case "Varna":
                if(amountSales >= 0 && amountSales <= 500){
                    commission = amountSales * 0.045;
                } else if (amountSales > 500 && amountSales <= 1000){
                    commission = amountSales * 0.075;
                }else if (amountSales > 1000 && amountSales <= 10000){
                    commission = amountSales * 0.10;
                }else if(amountSales > 10000){
                    commission = amountSales * 0.13;
                }else {
                    valid = false;
                }
                break;
            default:
                valid = false;
        }

        if(valid){
            System.out.printf("%.2f", commission);
        }else {
            System.out.println("error");
        }
    }
}
