import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n,k;
    static int[] weights, values;

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        k=Integer.parseInt(st.nextToken());
        weights= new int[n+1];
        values= new int[n+1];

        for (int i = 1; i < n+1; i++) {
            st= new StringTokenizer(br.readLine());
            weights[i]=Integer.parseInt(st.nextToken());
            values[i]=Integer.parseInt(st.nextToken());
        }

        int D[][]= new int[n+1][k+1];

        for (int i = 1; i < n+1; i++) {
            for (int w = 1; w < k+1; w++) {
                if(weights[i]>w){
                    D[i][w]= D[i-1][w];
                }
                else{
                    D[i][w]= Math.max(D[i-1][w], values[i]+D[i-1][w-weights[i]]);
                }
            }
        }

        System.out.println(D[n][k]);


    }
}