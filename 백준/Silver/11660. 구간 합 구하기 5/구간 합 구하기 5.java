import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
  public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      //숫자 저장하기기
      int arr[][] = new int[n+1][n+1];
      for (int i = 1; i<n+1; i++){
          st = new StringTokenizer(br.readLine());
          for (int j =1; j<n+1;j++){
              arr[i][j] = Integer.parseInt(st.nextToken());
          }
      }
      //구간 합 구하기기
      int sumArr[][] = new int[n+1][n+1];
      for (int i = 1; i<n+1; i++){
          for (int j =1; j<n+1;j++){
              sumArr[i][j] = sumArr[i][j-1]+sumArr[i-1][j]-sumArr[i-1][j-1]+arr[i][j];
          }
      }
      for(int i=0;i<m;i++){
          st = new StringTokenizer(br.readLine());
          int x1 = Integer.parseInt(st.nextToken());
          int y1 = Integer.parseInt(st.nextToken());
          int x2 = Integer.parseInt(st.nextToken());
          int y2 = Integer.parseInt(st.nextToken());
          // 합 구하기
          int result = sumArr[x2][y2]-sumArr[x1-1][y2]-sumArr[x2][y1-1]+sumArr[x1-1][y1-1];
          System.out.println(result);
      }
  }
}