import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Town implements Comparable<Town>{
    int end;
    int time;

    public Town(int end, int time) {
        this.end = end;
        this.time = time;
    }

    @Override
    public int compareTo(Town o) {
        return time - o.time;
    }
}

public class Main {
    private static final int INF=Integer.MAX_VALUE;
    //n개 마을, 학생: x번째 마을까지 왕복 / 도로 m개
    static int n,m,x,s,e,t,result;
    static List<ArrayList<Town>> graph;
    static int[] distance;

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        x=Integer.parseInt(st.nextToken());

        graph=new ArrayList<>();
        for (int i = 0; i < n+1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st=new StringTokenizer(br.readLine());
            s=Integer.parseInt(st.nextToken());
            e=Integer.parseInt(st.nextToken());
            t=Integer.parseInt(st.nextToken());

            //생성자 순서에 맞게 넣어줄것
            graph.get(s).add(new Town(e,t));
        }

        result=0;
        for (int i = 1; i < n+1; i++) {
            int[] go=dijkstra(i);
            int[] back=dijkstra(x);
            //i에서 x까지, x에서 i까지
            result=Math.max(result, go[x]+back[i]);
        }
        System.out.println(result);

    }

    private static int[] dijkstra(int start){
        PriorityQueue<Town> q=new PriorityQueue<>();
        distance= new int[n+1];
        Arrays.fill(distance, INF);

        distance[start]=0;
        //생성자를 end, time순으로 해놓고 값을 반대로 삽입해서 오류 발생! 이 부분 주의할 것
        q.offer(new Town(start, 0));

        while (!q.isEmpty()){
            Town t1=q.poll();
            int now_t=t1.time;
            int now=t1.end;

            for (Town t2: graph.get(now)) {
                int next_t=t2.time;
                int next=t2.end;

                if (distance[next]> now_t+next_t){
                    distance[next]= now_t+next_t;

                    //end, time 순 지켜서 넣기
                    q.offer(new Town(next, distance[next]));
                }
            }
        }
        return distance;
    }
}