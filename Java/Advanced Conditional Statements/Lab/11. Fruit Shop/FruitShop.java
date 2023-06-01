import java.util.Scanner;

public class FruitShop {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String product = input.nextLine(), day = input.nextLine();
        double amount = Double.parseDouble(input.nextLine());
        double total = 0;
        boolean valid = true;

        switch(day){
            case "Monday":
            case "Tuesday":
            case "Wednesday":
            case "Thursday":
            case "Friday":
                if(product.equals("banana")){
                    total = amount * 2.50;
                }else if(product.equals("apple")){
                    total = amount * 1.20;
                }else if (product.equals("orange")){
                    total = amount * 0.85;
                }else if(product.equals("grapefruit")){
                    total = amount * 1.45;
                }else if(product.equals("kiwi")){
                    total = amount * 2.70;
                }else if(product.equals("pineapple")){
                    total = amount * 5.50;
                }else if(product.equals("grapes")){
                    total = amount * 3.85;
                }else {
                    valid = false;
                }
                break;
            case "Saturday":
            case "Sunday":
                if(product.equals("banana")){
                    total = amount * 2.70;
                }else if(product.equals("apple")){
                    total = amount * 1.25;
                }else if (product.equals("orange")){
                    total = amount * 0.90;
                }else if(product.equals("grapefruit")){
                    total = amount * 1.60;
                }else if(product.equals("kiwi")){
                    total = amount * 3.00;
                }else if(product.equals("pineapple")){
                    total = amount * 5.60;
                }else if(product.equals("grapes")){
                    total = amount * 4.20;
                }else {
                    valid = false;
                }
                break;

            default:
                valid = false;
        }

        if(valid){
            System.out.printf("%.2f", total);
        }else {
            System.out.println("error");
        }

    }
}
