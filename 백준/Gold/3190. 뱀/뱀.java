import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine()); //보드 크기
        int K = Integer.parseInt(br.readLine()); // 사과 개수

        int[][] matrix = new int[N+1][N+1];
        for(int i=0;i<K;i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            matrix[x][y] = 1; // 사과 있음
        }

        int L = Integer.parseInt(br.readLine()); // 변환 횟수
        Deque<int[]> direction = new ArrayDeque<>();
        for(int i=0;i<L;i++){
            st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            char C = st.nextToken().charAt(0);
            if(C=='L'){ //왼쪽
                direction.add(new int[]{X,0});
            }else if(C=='D'){ //오른쪽
                direction.add(new int[]{X,1});
            }
        }

        int time=0;

        int[] pair = direction.poll();
        int turnTime = pair[0];
        int turnDir = pair[1];

        //상우하좌
        int[] dx = {-1,0,1,0};
        int[] dy = {0,1,0,-1};

        int dir = 1; //머리 방향, 오른쪽 방향으로 시작
        int headX = 1;
        int headY = 1;

        //뱀의 몸통 deque
        Deque<int[]> body = new ArrayDeque<>();

        //시뮬 시작
        while(true){
            time++;

            //머리를 다음 칸에 위치
            body.add(new int[]{headX,headY}); // 원래 머리가 있던 자리는 몸이 위치
            matrix[headX][headY] = 2;
            headX += dx[dir];
            headY += dy[dir];
            //벽 부딪히면 게임 끝
            if(headX <1 || headY <1 || headX > N || headY > N) break;
            //몸 부딪히면 게임 끝
            if(matrix[headX][headY] == 2) break;
            //이동한 칸에 사과가 있으면 사과 없어지고 꼬리는 안 움직임
            if(matrix[headX][headY] == 1){
                matrix[headX][headY] = 0;
            }else{ //사과 없으면 몸길이 줄여서 꼬리가 위치한 칸 비움
                int[] temp = body.pollFirst();
                matrix[temp[0]][temp[1]] = 0;
            }

            //머리 돌리기
            if(time == turnTime){
                if(turnDir == 0){
                    //왼쪽일 경우
                    dir=(dir+3)%4;
                }else if(turnDir == 1){
                    //오른쪽일 경우
                    dir=(dir+1)%4;
                }
                if (!direction.isEmpty()) {
                    pair = direction.poll();
                    turnTime = pair[0];
                    turnDir = pair[1];
                }
            }
        }

        //게임이 끝나는 시간 출력
        System.out.println(time);
    }
}