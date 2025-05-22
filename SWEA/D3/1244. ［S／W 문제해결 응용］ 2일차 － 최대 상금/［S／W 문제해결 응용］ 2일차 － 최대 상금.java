
import java.util.*;
import java.io.*;

class Solution
{
    static int max;
	static int changeCnt;
	public static void main(String args[]) throws Exception
	{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int test_case = 1; test_case <= T; test_case++) {
			max=0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			String nums = st.nextToken();
			char[] numsArr = nums.toCharArray();
			changeCnt = Integer.parseInt(st.nextToken());
			
			Set<String>[] visited = new HashSet[changeCnt +1];
			for(int i=0; i<=changeCnt; i++) {
				visited[i] = new HashSet<>();
			}
			
			dfs(numsArr, 0, visited);
			
			//가장 큰 금액 출력
			System.out.println("#"+test_case+" "+max);
		}
	}
    
    public static void dfs(char[] arr, int depth, Set<String>[] visited) {
		if(depth == changeCnt) {
			max = Math.max(max, Integer.parseInt(new String(arr)));
			return;
		}
		
		String current = new String(arr);
		if(visited[depth].contains(current)) return;
		visited[depth].add(current);
		
		int len = arr.length;
		for(int i=0; i<len -1;i++) {
			for(int j=i+1;j<len;j++) {
				//교환
				char temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
				
				dfs(arr, depth+1, visited);
				
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
}