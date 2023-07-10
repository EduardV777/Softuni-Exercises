import java.util.Scanner;

public class PinCodes {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        boolean valid = true;
        int limit1 = Integer.parseInt(input.nextLine());
        int limit2 = Integer.parseInt(input.nextLine());
        int limit3 = Integer.parseInt(input.nextLine());

        for(int k = 2; k <= limit1 ; k++){
            if(k % 2 == 0){

                for(int j = 2; j <= limit2; j++){
                    valid = true;
                    //check the validity of the middle number
                    for(int c = 2; c < limit2; c++) {
                        if (j != c && j % c == 0) {
                            valid = false;
                            break;
                        }
                    }
                    if(valid){
                        for (int i = 2; i <= limit3; i++) {
                            if (i % 2 == 0) {
                                System.out.printf("%d %d %d\n", k, j, i);
                            }
                        }
                    }
                }
            }
        }
    }
}
