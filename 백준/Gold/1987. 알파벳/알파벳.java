import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static int R,C, cnt,result,flag;
    static char[][] map;
    static int[] dx=new int[]{0,1,0,-1};
    static int[] dy=new int[]{1,0,-1,0};
    static boolean[] isVisited;


    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        R=Integer.parseInt(st.nextToken());
        C=Integer.parseInt(st.nextToken());
        isVisited=new boolean[26];


        map=new char[R][C];
        cnt=0;
        result=0;
        flag=0;
        for (int i = 0; i < R; i++) {
            String[] str=br.readLine().split("");
            for (int j = 0; j < C; j++) {
                map[i][j]= str[j].charAt(0);
            }
        }
        dfs(0,0,0);
        System.out.println(result);
    }

    private static void dfs(int r,int c, int cnt){

        if(isVisited[map[r][c]-'A']){ //방문했으면 그곳까지의 거리값을저장
            result=Math.max(result,cnt);
            return;
        }

        if(!isVisited[map[r][c]-'A']){
            isVisited[map[r][c]-'A']=true;
            for (int i = 0; i < 4; i++) {
                int nx=r+dx[i];
                int ny=c+dy[i];
                if(nx>=0 && nx<R && ny>=0 && ny<C) {
                    dfs(nx, ny, cnt + 1);
                }
            }
            isVisited[map[r][c]-'A']=false;
        }
    }
}