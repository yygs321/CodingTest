import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String me = sc.next();
        String doctor = sc.next();
        //h의 위치
        if(me.indexOf("h")>= doctor.indexOf("h"))
            System.out.println("go");
        else
            System.out.println("no");
    }
}