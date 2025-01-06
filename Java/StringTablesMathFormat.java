package TestingEdu;
import java.util.Scanner;
public class StringTablesMathFormat {
    public static void main(String[] args) {
    	Scanner obj = new Scanner(System.in);
        String[] table = new String[7];
        table[0] = obj.nextLine(); // Name Of Player
        table[1] = obj.nextLine();    // Number Of Year
        table[2] = obj.nextLine();      // Month Date
        table[3] = obj.nextLine();      // Day of birth
        table[4] = obj.nextLine();    // Current Bank Amount
        table[5] = obj.nextLine();      // Count of Cherry Bought
        table[6] = obj.nextLine();       // Price For One Cherry
        System.out.println(String.format("Hello %s, \n" +
	        "Since you were born %s Years, %s Months, and %s days \n" +
	        "You Have $%s In Your Bank \n" +
	        "But You Bought x%s Cherrys and one cherry is %s and Total For 20 is %s \n" +
	        "Now Your Bank is $%s",
            table[0], table[1], table[2], table[3], formatNumber(Integer.parseInt(table[4])),
            table[5], table[6], formatNumber(multiply(Integer.parseInt(table[5]), table[6])),
            formatNumber(Integer.parseInt(table[4]) - multiply(Integer.parseInt(table[5]), table[6]))
        ));
    }
    private static String formatNumber(int number) {
        return String.format("%,d", number);
    }

    private static int multiply(int amount, String price) {
        int numericPrice = Integer.parseInt(price);
        return (int) Math.floor(amount * numericPrice);
    }
}
