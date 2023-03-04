import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int R,C, answer;
    static int[][] map;
    static int[][] visited;

    static int[] dr={-1,1,0,0};
    static int[] dc={0,0,-1,1};
    static Queue<Pair> q;

    static class Pair{
        int r;
        int c;
        int day;

        public Pair(int r, int c, int day) {
            this.r = r;
            this.c = c;
            this.day=day;
        }
    }

    //익은 토마토 여러개가 동시에 돌아야하기 때문에 바로 큐에 넣어야함
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        //상자 가로 R, 세로 C
        C=Integer.parseInt(st.nextToken());
        R=Integer.parseInt(st.nextToken());

        visited=new int[R][C];

        answer=0;

        map=new int[R][C];
        //익은 토마토 1, 익지않은 토마토 0, 빈공간 -1
        q= new LinkedList<>();

        for (int i = 0; i < R; i++) {
            st=new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                map[i][j]=Integer.parseInt(st.nextToken());
                if(map[i][j]==1){
                    //익은 토마토 여러개가 동시에 돌아야하기 때문에 바로 큐에 넣어야함
                    q.offer(new Pair(i,j,0));
                }
            }
        }

        System.out.println(bfs());

    }

    private static int bfs(){
        answer=0;

        while(!q.isEmpty()){
            Pair p=q.poll();
            int x=p.r;
            int y=p.c;
            int d=p.day;

            for (int i = 0; i < 4; i++) {
                int nr=x+dr[i];
                int nc=y+ dc[i];
                if(nr>=0 && nr<R && nc>=0 && nc<C && map[nr][nc]==0){

                    map[nr][nc]=1;
                    answer=d+1;
                    q.offer(new Pair(nr,nc, d+1));
                }
            }
        }
        //토마토가 모두 익지 못하는 상황
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if(map[i][j]==0){
                    return -1;
                }
            }
        }
        return answer;
    }

}