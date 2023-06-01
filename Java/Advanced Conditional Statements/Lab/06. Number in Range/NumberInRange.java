import java.util.Scanner;

public class NumberInRange {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int num = Integer.parseInt(input.nextLine());
        boolean yesNo = false;

        if(num >= -100 && num <= 100){
            if(num != 0){
                yesNo = true;
            }
        }

        if(yesNo){
            System.out.println("Yes");
        } else{
            System.out.println("No");
        }
    }
}
