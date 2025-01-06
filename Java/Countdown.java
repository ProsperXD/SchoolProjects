package TestingEdu;
import java.util.Scanner;

public class Countdown
{
   public static void main(String[] args)
   {
      Scanner in = new Scanner(System.in);
      int n = in.nextInt();

        // Countdown loop
        for (int i = n; i >= 0; i--) {
            System.out.print(i); // Print the current number
            if (i > 0) {
                System.out.print("... "); // Print "..." followed by a space after the number, except for 0
            } else {
                System.out.print("Liftoff"); // Print "Liftoff" after 0
            }
        }
        System.out.println(); // Print a newline after the countdown

   }
}
