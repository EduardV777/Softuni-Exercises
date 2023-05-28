import java.util.Scanner;

public class TimePlus15Mins {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int hours = Integer.parseInt(input.nextLine());
        int minutes = Integer.parseInt(input.nextLine());

        int totalTimeMins = (hours * 60) + minutes + 15;

        hours = totalTimeMins / 60;
        minutes = totalTimeMins - (hours * 60);

        if(hours == 24){
            hours = 0;
        }

        String finalTimeStr = hours + ":";

        if(minutes < 10){
            finalTimeStr += "0";
        }

        finalTimeStr += minutes;

        System.out.printf("%s", finalTimeStr);
    }
}
