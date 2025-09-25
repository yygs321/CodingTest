import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static final int INF=Integer.MAX_VALUE;
    static int V, E;
    static HashMap<Integer,ArrayList<Pair>> map;
    static int[] distance;
    static boolean[] visited;

    static class Pair {
        int i, w;

        Pair(int i, int w) {
            this.i = i;
            this.w = w;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V=Integer.parseInt(st.nextToken());
        E=Integer.parseInt(st.nextToken());

        int start=Integer.parseInt(br.readLine());

        distance=new int[V+1];
        Arrays.fill(distance, INF);
        visited=new boolean[V+1];

        //map: arrayList 안에 또 arrayList -> hashmap으로 구현
        map=new HashMap<>();
        for (int i = 1; i < V + 1; i++) {
            map.put(i, new ArrayList<>());
        }


        for (int i = 0; i < E; i++) {
            st=new StringTokenizer(br.readLine());
            //from-> to 로 가는 가중치 w
            int from=Integer.parseInt(st.nextToken());
            int to=Integer.parseInt(st.nextToken());
            int w= Integer.parseInt(st.nextToken());

            map.get(from).add(new Pair(to, w));
        }

        distance[start]=0;

        int min,current;
        for (int i = 1; i < V+1; i++) {
            current=-1;
            min=INF;
            for (int j = 1; j < V+1; j++) {
                if(!visited[j] && min>distance[j]){
                    min=distance[j];
                    current=j;
                }
            }

            if(current==-1) break;



            visited[current]=true;
            for (Pair p: map.get(current)) {
                if (!visited[p.i] && p.w!=0 && distance[p.i]> min+p.w){
                    distance[p.i]= min+p.w;
                }
            }
        }

        for (int i = 1; i < V+1; i++) {
            System.out.println(distance[i]!=INF ? distance[i]: "INF" );
        }

    }
}