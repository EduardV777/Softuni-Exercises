import java.util.Scanner;

public class LunchBreak {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String seriesTitle = input.nextLine();
        int episodeLength = Integer.parseInt(input.nextLine());
        int restLength = Integer.parseInt(input.nextLine());

        double lunchTime = (double) restLength / 8, restTime = (double) restLength / 4;

        double totalTime = lunchTime + restTime + episodeLength;

        if(totalTime > restLength) {
            System.out.printf("You don't have enough time to watch %s, you need %d more minutes.", seriesTitle, (int) Math.ceil(totalTime - restLength));
        } else {
            System.out.printf("You have enough time to watch %s and left with %d minutes free time.", seriesTitle, (int) Math.ceil(restLength - totalTime));
        }
    }
}

/*
Game of Thrones
60
96
*/
