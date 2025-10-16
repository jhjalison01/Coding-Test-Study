import java.io.*;
import java.util.*;


class Main {
    static int N;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx ={-1,1,0,0};
    static int[] dy ={0,0,-1,1};
    static ArrayList<Integer> arr = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        visited = new boolean[N][N];

        for(int i=0; i<N; i++){
            String row = br.readLine();
            for(int j=0; j<N; j++){
                graph[i][j] = row.charAt(j) - '0';
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(!visited[i][j] && graph[i][j] == 1){
                    visited[i][j]=true;
                    arr.add(bfs(i,j));
                }
            }
        }

        System.out.println(arr.size());
        Collections.sort(arr);
        for(int k:arr){
            System.out.println(k);
        }

    }

    public static int bfs(int a, int b){
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{a, b});
        int cnt=1;

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx<0 || ny<0 || nx>=N || ny>=N){
                    continue;
                }

                if(graph[nx][ny] == 1 && !visited[nx][ny]){
                    visited[nx][ny] = true;
                    cnt+=1;
                    q.add(new int[]{nx, ny});
                }
            }
        }
        return cnt;
    }
}