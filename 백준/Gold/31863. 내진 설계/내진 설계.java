import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); //팀의 수
        int M = Integer.parseInt(st.nextToken()); // 경기의 수

        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};
        int collapsedCnt = 0;
        int notCollapsedCnt = 0;
        int[][]  board = new int[N][M];
        Deque<int[]> queue = new ArrayDeque<>();

        //board 채우기
        for(int i=0; i<N; i++){
            String row = br.readLine();
            for(int j=0; j<M; j++){
                char c = row.charAt(j);

                if(c == '@')
                    queue.add(new int[]{i,j,2}); //위치, 피해 범위
                else if(c == '.')
                    board[i][j] = 0;
                else if(c == '*'){
                    board[i][j] = 1;
                    notCollapsedCnt++;
                }
                else if(c == '#'){
                    board[i][j] = 2;
                    notCollapsedCnt++;
                }
                else
                    board[i][j] = 3;
            }
        }

        //bfs 
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            int w = cur[2];

            for(int i=0; i<4; i++){
                for(int k=1; k<=w; k++){
                    int nx = x + dx[i]*k;
                    int ny = y + dy[i]*k;
                    //지역 밖으로 나갈 경우 막힘
                    if(nx<0 || ny<0 || nx>=N || ny>=M) break;
                    //방파제일 경우 막힘
                    if(board[nx][ny] == 3) break;
                    //일반 도로일 경우 이어서 진행
                    if(board[nx][ny] == 0) continue;
                    //건물일 경우
                    if(board[nx][ny]<=2) board[nx][ny]--;
                    //{nx,ny} 건물이 부서졌을 경우
                    if(board[nx][ny]==0){
                        queue.add(new int[]{nx,ny,1});
                        collapsedCnt++;
                        notCollapsedCnt--;
                    }
                }
            }
        }

        //무너진 건물 개수, 무너지지 않은 건물 개수 출력
        System.out.println(collapsedCnt+" "+notCollapsedCnt);
        br.close();
    }
}