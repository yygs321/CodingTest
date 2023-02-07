import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt()+1;
        int[] slen = new int[n];

        for (int i = 1; i < n; i++) {
            slen[i] = sc.nextInt();
        }
        int student = sc.nextInt();

        for(int j = 1; j<= student; j++) {
            int sx = sc.nextInt();
            int m = sc.nextInt();

            if(sx == 1) {
                for(int i = m; i<n; i+=m) {
                    slen[i] = slen[i]==0 ? 1:0;
                }
            }

            else if(sx == 2){
                int l = m-1;
                int r = m+1;

                while(true) {//대칭 찾아서
                    if(l<1 || r>= n) break;
                    if(slen[l] != slen[r]) break;
                    l--; r++;
                }
                l++; r--;

                while(l<=r) {
                    slen[l] = slen[l]==0 ? 1:0;
                    l++;
                }
            }
        }

        for (int i = 1; i < n; i++) {
            System.out.print(slen[i]+" ");
            if(i%20==0) System.out.println();
        }

    }
}