import java.util.Scanner;

public class Workout {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int workoutDays = Integer.parseInt(input.nextLine());
        double distRunKm = Double.parseDouble(input.nextLine());
        double totalKmRan = distRunKm;

        while(workoutDays != 0){
            int distIncrease = Integer.parseInt(input.nextLine());
            distRunKm += distRunKm * ((double) distIncrease / 100);
            totalKmRan += distRunKm;
            workoutDays--;
        }

        if(totalKmRan >= 1000){
            System.out.printf("You've done a great job running %.0f more kilometers!", Math.ceil(totalKmRan - 1000));
        }else {
            System.out.printf("Sorry Mrs. Ivanova, you need to run %.0f more kilometers", Math.ceil(1000 - totalKmRan));
        }
    }
}
