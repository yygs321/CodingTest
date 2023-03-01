import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    N개의 구역(1-N번 구역)
    각 구역은 두 선거구 중 하나에 포함
    선거구는 적어도 한개의 구역 포함: 구역 1개이상
    동일 선거구 구역은 모두 연결
    되도록 선거구를 나눠야함 (현재상태: 모두 1로 연결)
    -> 인구차이의 최솟값 출력
     */
    static int N, result;
    static HashMap<Integer, List<Integer>> map;
    static boolean[] isSelected,visited;

    static int[] pp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //구역 개수 N
        N = Integer.parseInt(br.readLine());

        result = Integer.MAX_VALUE;
        isSelected= new boolean[N + 1];

        pp = new int[N + 1]; //인구수
        //구역 인구
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            pp[i] = Integer.parseInt(st.nextToken());
        }

        map = new HashMap<>();
        //선거구
        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine());
            map.put(i, new ArrayList<>());
            // 첫번째값: 인접한 개수 m / 이후: 인접구역
            int m = Integer.parseInt(st.nextToken());
            for (int j = 1; j <= m; j++) {
                int x = Integer.parseInt(st.nextToken());
                map.get(i).add(x);
            }
        }

        subset(1); // 정점이므로 cnt= 1~N까지 사용

        if(result==Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else{
            System.out.println(result);
        }
    }

    private static void subset(int cnt){
        if(cnt==N+1){ //N까지 다 고르고 넘어온것
            //부분집합을 다 골랐으면 유효한지 검사(선거구 1개에 최소 1개의 구역)
            solve();
            return;
        }

        isSelected[cnt]=true;
        subset(cnt+1);
        isSelected[cnt]=false;
        subset(cnt+1);
    }

    private static void solve(){
        List<Integer> alist = new ArrayList<>();
        List<Integer> blist = new ArrayList<>();

        for (int i = 1; i < N + 1; i++) {
            if (isSelected[i]) {
                alist.add(i);
            } else {
                blist.add(i);
            }
        }

        //한 선거구가 구역이 한개라도 없으면 return
        if (alist.size() == 0 || blist.size() == 0) {
            return;
        }

        //각 구역에 해당하는 값에만 visited를 했을 때 전체구역이 속해있는지 판별
        visited = new boolean[N + 1];
        bfs(alist);
        bfs(blist);

        //alist, blist 다 돌았으면 전부 방문되어있어야함
        //전체 구역 포함하는지 판별
        for (int i = 1; i < N + 1; i++) {
            if(!visited[i]) return;
        }

        //구역끼리 잘 연결되어있으면 인구 계산
        count(alist);
    }

    private static void count(List<Integer> alist){
        //구역끼리 잘 연결되어있으면 인구 계산
        int app=0;
        int bpp=0;
        for (int i = 1; i < N + 1; i++) {
            if(alist.contains(i)){
                app+=pp[i];
            }else{
                bpp+=pp[i];
            }
        }

        result=Math.min(result, Math.abs(app-bpp));
    }

    private static void bfs(List<Integer> lst){
        Queue<Integer> queue=new LinkedList<>();

        //골라온 부분집합 값을 탐색
        int x= lst.get(0);
        queue.add(x);
        visited[x]=true;

        while(!queue.isEmpty()){
            int q=queue.poll();
            for (Integer in : map.get(q)) {
                //연결된 값들 중에 구역에 해당하는 값만 방문처리하고
                //해당 구역에 또 연결된 곳들을 탐색하기 위해 queue에 추가
                //lst에 포함되어있고, 방문되지 않은 곳
                if(lst.contains(in) && !visited[in]){
                    visited[in]=true;
                    queue.offer(in);
                }
            }
        }

    }

}