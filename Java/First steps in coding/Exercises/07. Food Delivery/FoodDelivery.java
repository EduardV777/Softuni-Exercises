import java.util.Scanner;
public class FoodDelivery {
    public static void main(String[] args){
        //prices
        double chickenMenuPrice = 10.35;
        double fishMenuPrice = 12.40;
        double vegetarianMenuPrice = 8.15;
        double dessertPrice = 0; //20% of total sum, delivery excluded
        double deliveryPrice = 2.50;

        Scanner input = new Scanner(System.in);

        int chickenMenus = Integer.parseInt(input.nextLine());
        int fishMenus = Integer.parseInt(input.nextLine());
        int vegetarianMenus = Integer.parseInt(input.nextLine());

        double orderTotal = ((double)chickenMenus * chickenMenuPrice) + ((double)fishMenus * fishMenuPrice) + ((double)vegetarianMenus * vegetarianMenuPrice);
        dessertPrice = orderTotal * 0.2;
        orderTotal += dessertPrice + deliveryPrice;

        System.out.println(orderTotal);
    }
}
