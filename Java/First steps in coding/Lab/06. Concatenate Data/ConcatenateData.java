import java.util.Scanner;

public class ConcatenateData {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        String firstName = input.nextLine();
        String lastName = input.nextLine();
        String age = input.nextLine();
        String city = input.nextLine();

        String output = "You are " + firstName + " " + lastName + ", a " + age + "-years old person from " + city + ".";
        System.out.println(output);
    }
}
