import java.util.Scanner;

public class WorkingHours {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int time = Integer.parseInt(input.nextLine());
        String day = input.nextLine();
        boolean open = false;

        switch(day){
            case "Monday":
            case "Tuesday":
            case "Wednesday":
            case "Thursday":
            case "Friday":
            case "Saturday":
                if(time >= 10 && time <= 18){
                    open = true;
                }
                break;
        }

        if(open){
            System.out.println("open");
        }else {
            System.out.println("closed");
        }
    }
}
