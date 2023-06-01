import java.util.Scanner;

public class AnimalType {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String animalName = input.nextLine();

        switch(animalName){
            case "dog":
                System.out.println("mammal");
                break;
            case "crocodile":
            case "tortoise":
            case "snake":
                System.out.println("reptile");
                break;
            default:
                System.out.println("unknown");
        }
    }
}
