import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int[] arr = new int[a];
        int length = 0;
        int st_a = 0;


        for (int i=0; i<a; i++){
            String now = sc.next();
            length += now.length();
            if (now.charAt(0)=='a'){
                st_a ++;
            }
        }

        System.out.print(length + " " + st_a); 
    }
}