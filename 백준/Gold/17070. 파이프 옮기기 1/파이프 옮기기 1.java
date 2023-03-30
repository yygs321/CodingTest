import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n,result;
    static int[][] home;

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        result=0;

        home= new int[n+1][n+1];
        for (int i = 1; i < n+1; i++) {
            st=new StringTokenizer(br.readLine());
            for (int j = 1; j < n+1; j++) {
                home[i][j]= Integer.parseInt(st.nextToken());
            }
        }
        dfs(0,1,2);
        System.out.println(result);

    }
    private static void dfs(int line, int r, int c){
        if (r==n && c==n){
            result++;
            return;
        }

        switch (line){ // 가로 0, 세로1, 대각선2
            case 0:
                if (c+1<=n && home[r][c+1]==0){
                    dfs(0, r, c+1); // 가로
                }
                break;
            case 1:
                if (r+1<=n && home[r+1][c]==0){
                    dfs(1, r+1, c);
                }
                break;
            case 2:
                if (c+1<=n && home[r][c+1]==0) {
                    dfs(0, r, c + 1);
                }
                if (r+1<=n&& home[r+1][c]==0){
                    dfs(1, r+1,c);
                }
                break;
        }
        if (r+1<=n && c+1<=n && home[r+1][c+1]==0 && home[r][c+1]==0 && home[r+1][c]==0){
            dfs(2, r+1, c+1); //대각선은 무조건 실행
        }
    }
}