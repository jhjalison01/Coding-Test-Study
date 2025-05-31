import java.io.*;

public class Main {
    static StringBuilder answer=new StringBuilder();
    static int[][] matrix;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        //matrix 받기
        matrix = new int[N][N];
        for(int i = 0; i < N; i++){
            String line = br.readLine();
            for(int j = 0; j < N; j++){
                matrix[i][j] = line.charAt(j)-'0';
            }
        }

        solve(0,0,N);
        System.out.println(answer.toString());
    }

    public static void solve(int x, int y, int size){
        //영역이 모두 같은 숫자인지 확인
        if(isSame(x, y, size)){
            answer.append(matrix[x][y]);
            return;
        }

        answer.append('(');
        int newSize = size/2;

        solve(x,y, newSize); //왼쪽 위
        solve(x,y+newSize,newSize); // 오른쪽 위
        solve(x+newSize,y,newSize); //왼쪽 아래
        solve(x+newSize,y+newSize,newSize);

        answer.append(')');
    }

    public static boolean isSame(int x, int y, int size){
        int first = matrix[x][y];

        for(int i=x; i<x+size; i++){
            for(int j=y; j<y+size; j++){
                if(matrix[i][j] != first) return false;
            }
        }
        return true;
    }
}