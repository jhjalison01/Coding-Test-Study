import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    //N,M 입력 받기기
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    //누적 합 구하기
    int[] arr = new int[n+1];
    st = new StringTokenizer(br.readLine());
    for(int i=1;i<n+1;i++){
        arr[i]=arr[i-1]+Integer.parseInt(st.nextToken());
    }
    //구간 합 구하기
    for(int q=0; q<m;q++){
        st = new StringTokenizer(br.readLine());
        int i = Integer.parseInt(st.nextToken());
        int j = Integer.parseInt(st.nextToken());
        System.out.println(arr[j]-arr[i-1]);
    }
  }
}