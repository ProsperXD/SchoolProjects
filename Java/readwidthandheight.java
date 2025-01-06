package TestingEdu;
import java.util.Scanner;
public class ReadswidthAndHeight{
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Wall width: ");
        double wallWidth = scanner.nextDouble();

        System.out.print("Wall height: ");
        double wallHeight = scanner.nextDouble();

        System.out.print("Number of windows: ");
        int numberOfWindows = scanner.nextInt();

        scanner.close();

        double windowArea = 2 * 3;

        double totalWindowsArea = numberOfWindows * windowArea;

        double area = wallWidth * wallHeight - totalWindowsArea;

        System.out.println("Area: " + area);
	}
}
