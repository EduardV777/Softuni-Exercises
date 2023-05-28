import java.util.Scanner;

public class SumSeconds {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int firstCompetitorSeconds = Integer.parseInt(input.nextLine());
        int secondCompetitorSeconds = Integer.parseInt(input.nextLine());
        int thirdCompetitorSeconds = Integer.parseInt(input.nextLine());


        int totalTime = firstCompetitorSeconds + secondCompetitorSeconds + thirdCompetitorSeconds;
        int totalMins = totalTime / 60;
        int totalSeconds = totalTime - (totalMins * 60);

        String totalTimeStr = totalMins + ":";

        if (totalSeconds < 10){
            totalTimeStr += "0";
        }

        totalTimeStr += totalSeconds;

        System.out.println(totalTimeStr);
    }
}

/*
35
45
44
*/
