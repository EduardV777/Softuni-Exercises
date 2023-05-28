import java.util.Scanner;
public class AreaOfFigures {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //square rectangle circle triangle
        String typeOfFigure = input.nextLine();
        double area = 0;

        if(typeOfFigure.equals("square")){
            double length = Double.parseDouble(input.nextLine());
            area = length * length;

        }else if (typeOfFigure.equals("rectangle")){
            double width = Double.parseDouble(input.nextLine());
            double length = Double.parseDouble(input.nextLine());
            area = width * length;

        }else if (typeOfFigure.equals("circle")){
            double radius = Double.parseDouble(input.nextLine());
            area = Math.PI * Math.pow(radius, 2);

        }else if (typeOfFigure.equals("triangle")){
            double length = Double.parseDouble(input.nextLine());
            double height = Double.parseDouble(input.nextLine());

            area = (length / 2) * height;
        }

        System.out.printf("%.3f", area);
    }
}
