import java.util.*;
import java.io.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T=10;
        StringTokenizer st;
        
		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[] arr = new int[N];
            for(int i =0;i<N;i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }
            int answer = 0;
            for(int i=2; i<N-2; i++){
                int[] temp = {arr[i-2], arr[i-1], arr[i+1], arr[i+2]};
                int max = Integer.MIN_VALUE;
                for(int val:temp){
                    max = Math.max(max, val);
                }
                if(arr[i]-max>0)
                    answer+=arr[i]-max;
            }
            System.out.println("#"+test_case+" "+answer);
		}
	}
}