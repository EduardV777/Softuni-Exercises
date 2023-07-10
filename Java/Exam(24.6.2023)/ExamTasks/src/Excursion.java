import java.util.Scanner;

public class Excursion {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double nightPrice = 20;
        double cardPrice = 1.60;
        double ticketPrice = 6;

        int people = Integer.parseInt(input.nextLine());
        int nights = Integer.parseInt(input.nextLine());
        int transportCards = Integer.parseInt(input.nextLine());
        int museumTickets = Integer.parseInt(input.nextLine());

        //add additional 25% for unexpected expenses

        double totalCost = (nights * nightPrice * people) + (cardPrice * transportCards * people) + (ticketPrice * museumTickets * people);
        totalCost += totalCost * 0.25;
        System.out.printf("%.2f", totalCost);
    }
}