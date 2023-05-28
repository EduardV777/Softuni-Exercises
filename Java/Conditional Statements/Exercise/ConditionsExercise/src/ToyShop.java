import java.util.Scanner;

public class ToyShop {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double puzzlePrice = 2.60, talkingDollPrice = 3.00, teddyBearPrice = 4.10, minionPrice = 8.20, toyTruckPrice = 2.00;

        double tourCost = Double.parseDouble(input.nextLine());
        int puzzles = Integer.parseInt(input.nextLine());
        int dolls = Integer.parseInt(input.nextLine());
        int teddyBears = Integer.parseInt(input.nextLine());
        int minions = Integer.parseInt(input.nextLine());
        int trucks = Integer.parseInt(input.nextLine());

        int orderedToys = puzzles + dolls + teddyBears + minions + trucks;

        double totalEarnings = (puzzles * puzzlePrice) + (dolls * talkingDollPrice) + (teddyBears * teddyBearPrice) + (minions * minionPrice) + (trucks * toyTruckPrice);

        //discount
        if(orderedToys >= 50){
            totalEarnings -= totalEarnings * 0.25;
        }

        //rent expenses
        totalEarnings -= totalEarnings * 0.1;

        if (totalEarnings >= tourCost) {
            System.out.printf("Yes! %.2f lv left.", totalEarnings - tourCost);
        } else {
            System.out.printf("Not enough money! %.2f lv needed.", tourCost - totalEarnings);
        }
    }
}


/*
⦁	Пъзел - 2.60 лв.
        ⦁	Говореща кукла - 3 лв.
        ⦁	Плюшено мече - 4.10 лв.
        ⦁	Миньон - 8.20 лв.
        ⦁	Камионче - 2 лв.
*/



/*
⦁	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
        ⦁	Брой пъзели - цяло число в интервала [0… 1000]
        ⦁	Брой говорещи кукли - цяло число в интервала [0 … 1000]
        ⦁	Брой плюшени мечета - цяло число в интервала [0 … 1000]
        ⦁	Брой миньони - цяло число в интервала [0 … 1000]
        ⦁	Брой камиончета - цяло число в интервала [0 … 1000]
*/


//Example input
/*
40.8
20
25
30
50
10
*/
