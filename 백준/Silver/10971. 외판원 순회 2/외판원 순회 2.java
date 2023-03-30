import java.util.Scanner;

public class Main {

    static int[][] cost;
    static boolean[] visited;
    static int answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        cost = new int[n][n];
        visited = new boolean[n];
        answer = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cost[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < n; i++) {
            visited[i] = true;
            dfs(i, i, 0, 1);
            visited[i] = false;
        }

        System.out.println(answer);
    }

    static void dfs(int start, int now, int value, int cnt) {
        int n = cost.length;
        if (cnt == n) {
            if (cost[now][start] != 0) {
                value += cost[now][start];
                answer = Math.min(answer, value);
            }
            return;
        }

        if (value > answer) {
            return;
        }

        for (int j = 0; j < n; j++) {
            if (now == j || visited[j] || cost[now][j] == 0) {
                continue;
            }
            visited[j] = true;
            dfs(start, j, value + cost[now][j], cnt + 1);
            visited[j] = false;
        }
    }
}