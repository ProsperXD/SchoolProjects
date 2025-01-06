package TestingEdu;
import java.util.Scanner;

public class RatWeight {
    public static void main(String[] args) {
        scnr in = new Scanner(System.in);
        int x;
        x = scnr.nextInt();
        if (x < 10) {
           System.out.print("Live ");
        }
        else if (x < 20) {
           System.out.print("long ");
        }
        else if (x < 30) {
           System.out.print("and ");
        }
        System.out.print("prosper!");
    }
}
