import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String l = sc.nextLine();

        String[] arr = l.split(" ");

        for (int i=0; i<arr.length; i+=2){
            System.out.println(arr[i]);
        }
    }
}