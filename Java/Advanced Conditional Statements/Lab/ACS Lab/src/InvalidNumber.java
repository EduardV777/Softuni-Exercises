import java.util.Scanner;

public class InvalidNumber {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int num = Integer.parseInt(input.nextLine());
        boolean valid = false;

        if((num >= 100 && num <= 200) || num == 0){
            valid = true;
        }

        if(!valid){
            System.out.println("invalid");
        }
    }
}
