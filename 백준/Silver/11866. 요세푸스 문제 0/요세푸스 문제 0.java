import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        StringBuilder sb= new StringBuilder("");

        int n=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());
        int cnt=0;

        ArrayList<Integer> answer=new ArrayList<>();
        Queue<Integer> ycps=new LinkedList<>();

        for (int i = 1; i < n+1; i++) {
            ycps.offer(i);
        }

        while (!ycps.isEmpty()){
            int q=ycps.poll();
            cnt++;
            if(cnt==k){
                answer.add(q);
                cnt=0;
                continue;
            }
            ycps.offer(q);
        }

        sb.append("<");
        for (int i = 0; i < n; i++) {
            if (i==n-1){
                sb.append(answer.get(i)+">");
                continue;
            }
            sb.append(answer.get(i)+", ");
        }

        System.out.println(sb);
    }
}