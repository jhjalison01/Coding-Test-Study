import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int MOD = 1000000007;

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] dp = new int[M+1][26]; // dp[i][j]: 길이 i, 마지막 알파벳 j

        //길이 1일 때는 모든 알파벳이 가능하므로 1로 초기화
        for(int j=0; j<26; j++){
            dp[1][j] = 1;
        }

        //dp 채우기
        for(int i=2; i<=M; i++){
            for(int j=0; j<26; j++){ //현재 위치에 놓일 알파벳
                for(int k=0;k<26;k++){ // 이전 위치 알파벳
                    if(Math.abs(j-k) >= N){
                        dp[i][j] = (dp[i][j]+dp[i-1][k])%MOD;
                    }
                }
            }
        }

        //길이 M에서 가능한 모든 마지막 알파벳의 경우를 합산
        int answer=0;
        for(int j=0; j<26; j++){
            answer=(answer+dp[M][j])%MOD;
        }

        System.out.println(answer);

        br.close();
    }
}