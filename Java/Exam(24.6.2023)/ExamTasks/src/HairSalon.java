import java.util.Scanner;

public class HairSalon {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int dayTarget = Integer.parseInt(input.nextLine());
        int earnings = 0;
        String type = "";

        while(earnings < dayTarget){
            String command = input.nextLine();

            if(command.equals("closed")){
                break;

            }else {
                switch(command){
                    case "haircut":
                        type = input.nextLine();

                        if(type.equals("mens")){
                            earnings += 15;
                        }else if(type.equals("ladies")){
                            earnings += 20;
                        }else if(type.equals("kids")){
                            earnings += 10;
                        }
                        break;

                    case "color":
                        type = input.nextLine();

                        if(type.equals("touch up")){
                            earnings += 20;
                        }else if(type.equals("full color")){
                            earnings += 30;
                        }
                        break;
                }
            }
        }

        if(earnings >= dayTarget){
            System.out.printf("You have reached your target for the day!\nEarned money: %dlv.", earnings);
        }else {
            System.out.printf("Target not reached! You need %dlv. more.\nEarned money: %dlv.", dayTarget - earnings, earnings);
        }
    }
}
