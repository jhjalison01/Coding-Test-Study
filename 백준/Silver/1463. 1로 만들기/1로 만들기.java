import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[N+1];

        //bottom up
        for(int i=2;i<N+1;i++){
            //현재 수에서 1을 빼는 경우
            dp[i] = dp[i-1]+1;
            //현재의 수가 2로 나누어 떨어질 경우
            if(i%2 == 0){
                dp[i] = Math.min(dp[i], dp[i/2]+1);
            }
            //현재의 수가 3으로 나누어 떨어질 경우
            if(i%3 == 0){
                dp[i] = Math.min(dp[i], dp[i/3]+1);
            }
        }

        System.out.println(dp[N]);
    }
}