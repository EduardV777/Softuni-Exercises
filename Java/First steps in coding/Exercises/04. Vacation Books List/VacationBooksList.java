import java.util.Scanner;

public class VacationBooksList {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int pages = Integer.parseInt(input.nextLine());
        int pagesPerHour = Integer.parseInt(input.nextLine());
        int daysToRead = Integer.parseInt(input.nextLine());

        int time = (pages / pagesPerHour) / daysToRead;

        System.out.println(time);
    }
}
