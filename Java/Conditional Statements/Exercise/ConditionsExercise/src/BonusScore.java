import java.util.Scanner;

public class BonusScore {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int initPoints = Integer.parseInt(input.nextLine());
        double bonusPoints = 0;

        if(initPoints <= 100){
            bonusPoints += 5;

        } else if (initPoints > 100 && initPoints <= 1000){
            bonusPoints += initPoints * 0.2;

        }else {
            bonusPoints += initPoints * 0.1;
        }

        if(initPoints % 2 == 0){
            bonusPoints += 1;
        } else if (initPoints % 5 == 0){
            bonusPoints += 2;
        }

        double totalPoints = (double) initPoints + bonusPoints;

        System.out.printf("%.1f\n%.1f", bonusPoints, totalPoints);
    }

}
