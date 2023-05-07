import java.util.Scanner;


public class Main {
    static int X,N;
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        X=sc.nextInt();
        N=sc.nextInt();

        int result=0;
        for (int i = 0; i < N; i++) {
            int a=sc.nextInt();
            int b=sc.nextInt();
            result+=a*b;
        }
        if (result==X){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }


    }
}