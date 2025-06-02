import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] arr = new int[N];
        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int tempSum =0;
        for(int i=0;i<K;i++){
            tempSum += arr[i];
        }

        int maxSum = tempSum;

        for(int i=K; i<N;i++){
            tempSum = tempSum - arr[i-K] + arr[i];
            maxSum = Math.max(maxSum, tempSum);
        }

        System.out.println(maxSum);
    }
}