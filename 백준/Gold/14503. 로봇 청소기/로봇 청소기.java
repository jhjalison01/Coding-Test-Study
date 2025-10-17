import java.io.*;
import java.util.*;


class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        //북동남서
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        //청소 유무
        boolean[][] visited = new boolean[N][M];
        //청소 영역 정보 받아오기
        int[][] graph = new int[N][M];
        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<M;j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer=0;
        boolean isEnd = false;

        while(true){
            if(isEnd) break;
            //현재 칸 청소
            if(!visited[x][y]){
                visited[x][y] = true;
                answer++;
            }

            boolean isAllClean = true;
            //현재 칸의 주변 4칸 탐색
            for(int i=0;i<4;i++){
                //반시계 방향으로 90도 회전
                d = (d+3)%4;
                int nx = x+dx[d];
                int ny = y+dy[d];

                if(nx<0 || ny<0 || nx>=N || ny>=M) continue;
                //청소하지 않은 칸으로 전진
                if(!visited[nx][ny] && graph[nx][ny]==0){
                    x = nx;
                    y = ny;
                    isAllClean = false;
                    break;
                }
            }

            //주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            if(isAllClean){
                // 현재 방향을 유지한 채로 한 칸 후진
                // 북(0)->남(2), 동(1)->서(3), 남(2)->북(0), 서(3)->동(1)
                int rd = (d+2)%4;
                int rx = x+dx[rd];
                int ry = y+dy[rd];
                //뒤로 후진할 수 없는 경우
                if(graph[rx][ry]==1){
                    isEnd = true; //종료
                }else{
                    x = rx;
                    y = ry;
                }
            }
        }

        System.out.println(answer);
    }
}