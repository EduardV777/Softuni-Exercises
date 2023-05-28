import java.util.Scanner;

public class Shopping {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double budget = Double.parseDouble(input.nextLine());
        int videoCards = Integer.parseInt(input.nextLine());
        int processors = Integer.parseInt(input.nextLine());
        int rams = Integer.parseInt(input.nextLine());

        //prices
        double gpuPrice = 250, cpuPrice = ((videoCards * gpuPrice) * 0.35), ramPrice = ((videoCards * gpuPrice) * 0.1);

        double totalExpenses = (videoCards * gpuPrice) + (processors * cpuPrice) + (rams * ramPrice);

        if(videoCards > processors){
            totalExpenses -= totalExpenses * 0.15;
        }

        if(totalExpenses > budget) {
            System.out.printf("Not enough money! You need %.2f leva more!", totalExpenses - budget);
        }else {
            System.out.printf("You have %.2f leva left!", budget - totalExpenses);
        }
    }
}

/*
⦁	Видеокарта – 250 лв./бр.
        ⦁	Процесор – 35% от цената на закупените видеокарти/бр.
        ⦁	Рам памет – 10% от цената на закупените видеокарти/бр.
*/

/*
⦁	Бюджетът на Петър - реално число в интервала [0.0…100000.0]
        ⦁	Броят видеокарти - цяло число в интервала [0…100]
        ⦁	Броят процесори - цяло число в интервала [0…100]
        ⦁	Броят рам памет - цяло число в интервала [0…100]
*/

//example input
/*
900
2
1
3
*/
