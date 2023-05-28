import java.util.Scanner;

public class WorldSwimmingRecord {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double recordSec = Double.parseDouble(input.nextLine());
        double metersDist = Double.parseDouble(input.nextLine());
        double swimMeterSec = Double.parseDouble(input.nextLine());

        //water resistance slows down the competitor every 15 meters by 12.5 seconds

        int slowdowns = (int) Math.floor(metersDist / 15);

        double totalTimeSec = (swimMeterSec * metersDist) + (slowdowns * 12.5);

        if(totalTimeSec >= recordSec) {
            System.out.printf("No, he failed! He was %.2f seconds slower.", totalTimeSec - recordSec);
        } else {
            System.out.printf("Yes, he succeeded! The new world record is %.2f seconds.", totalTimeSec);
        }
    }
}


/*
10464
1500
20
*/
