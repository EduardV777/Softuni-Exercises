import java.util.Scanner;
public class ProjectsCreation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String architectName = input.nextLine();
        int projectsAmount = Integer.parseInt(input.nextLine()); //Each project takes 3 hrs
        int numberOfHours = projectsAmount * 3;

        System.out.printf("The architect %s will need %d hours to complete %d project/s.", architectName, numberOfHours, projectsAmount);
    }
}
