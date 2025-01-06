package TestingEdu;
import java.util.Scanner;
import java.util.InputMismatchException;

public class NameAgeChecker {
	   public static void main(String[] args) {
	      Scanner scnr = new Scanner(System.in);

	      String inputName;
	      int age;

	      inputName = scnr.next();
	      while (!inputName.equals("-1")) {
	    	  try {
	    		  age = scnr.nextInt();
	    		  System.out.println(inputName + " " + (age + 1));
	    		}
	    		catch(InputMismatchException e) {
	    			scnr.hasNextLine();
	    			System.out.println(inputName + " " + 0);
	    			inputName = scnr.nextLine();
	    		}
	         inputName = scnr.next();
	      }
	   }
	}
