import java.util.Scanner;

public class FruitOrVegetable {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String product = input.nextLine();
        String category;

        switch(product){
            case "banana":
            case "apple":
            case "kiwi":
            case "cherry":
            case "lemon":
            case "grapes":
                category = "fruit";
                break;
            case "tomato":
            case "cucumber":
            case "pepper":
            case "carrot":
                category = "vegetable";
                break;
            default:
                category = "unknown";
        }

        System.out.println(category);
    }
}
