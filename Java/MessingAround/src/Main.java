//author: Will Orme
import java.util.*;



public class Main {

    public static void main (String[] args) {

        //Prints largest of 3 numbers
        System.out.print("Enter a number: ");
        Scanner scn = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(scn.nextInt());
        System.out.print("Enter another number: ");
        scn.hasNextInt();
        numbers.add(scn.nextInt());
        System.out.print("Enter a third number: ");
        scn.hasNextInt();
        numbers.add(scn.nextInt());
        if (numbers.get(0) > numbers.get(1)) {
            if(numbers.get(0) > numbers.get(2)){
                System.out.println("The greatest: " + numbers.get(0));
            }
        }
        else if (numbers.get(1) > numbers.get(0)) {
            if(numbers.get(1) > numbers.get(2)){
                System.out.println("The greatest: " + numbers.get(1));
            }
        }
        else if (numbers.get(2) > numbers.get(0)){
            if(numbers.get(2) > numbers.get(1))
            System.out.println("The greatest: " + numbers.get(2));
            }
        else{
            System.out.println("Error, duplicate numbers.");;
        }
    }







}






















