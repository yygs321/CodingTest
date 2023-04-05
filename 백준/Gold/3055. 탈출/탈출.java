import java.io.BufferedReader;
import java.io.CharArrayReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static char[][] graph;
    static int[][] visited;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static Queue<Node> q1 = new LinkedList<>();
    static Queue<Node> q2 = new LinkedList<>();
    static int result = -1;

    static class Node {
        int x;
        int y;
        int cnt;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    static void bfs() {
        while (!q1.isEmpty()) {
            Node node = q1.poll();
            int x = node.x;
            int y = node.y;
            int cnt = node.cnt;
            visited[x][y] = cnt;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < graph.length && 0 <= ny && ny < graph[0].length) {
                    if (graph[nx][ny] == 'X') continue;
                    else if (visited[nx][ny] == -1 && graph[nx][ny] != 'D') {
                        visited[nx][ny] = visited[x][y] + 1;
                        graph[nx][ny] = '*';
                        q1.offer(new Node(nx, ny, cnt + 1));
                    }
                }
            }
        }
    }

    static void bfs2(int x, int y) {
        visited[x][y] = 0;
        q2.offer(new Node(x, y));

        while (!q2.isEmpty()) {
            Node node = q2.poll();
            x = node.x;
            y = node.y;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < graph.length && 0 <= ny && ny < graph[0].length) {
                    if (graph[nx][ny] == 'X') continue;
                    else if (graph[nx][ny] == 'D') {
                        result = visited[x][y] + 1;
                        return;
                    } else {
                        if (visited[nx][ny] != -1 && visited[nx][ny] <= visited[x][y] + 1) {
                            continue;
                        }
                        visited[nx][ny] = visited[x][y] + 1;
                        q2.offer(new Node(nx, ny, visited[x][y] + 1));
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        graph = new char[r][c];
        visited = new int[r][c];

        int x1 = -1, y1 = -1;
        for (int i = 0; i < r; i++) {
            String str = br.readLine();
            for (int j = 0; j < c; j++) {
                graph[i][j] = str.charAt(j);
                visited[i][j] = -1;

                if (graph[i][j] == 'S') {
                    x1 = i;
                    y1 = j;
                } else if (graph[i][j] == '*') {
                    q1.offer(new Node(i, j, 0));
                }
            }

        }
        bfs();
        bfs2(x1, y1);

        if (result == -1) {
            System.out.println("KAKTUS");
        } else {
            System.out.println(result);
        }
        
    }
}