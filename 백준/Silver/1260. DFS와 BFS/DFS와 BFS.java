import java.io.*;
import java.util.*;

public class Main {
    static boolean visited[];
    static ArrayList<Integer>[] arr;
  public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      int N = Integer.parseInt(st.nextToken());
      int M = Integer.parseInt(st.nextToken());
      int V = Integer.parseInt(st.nextToken());
      
      arr = new ArrayList[N+1];
      for(int i=1; i<N+1; i++){
          arr[i]=new ArrayList<Integer>();
      }
      for(int i=0; i<M; i++){
          st = new StringTokenizer(br.readLine());
          int a = Integer.parseInt(st.nextToken());
          int b = Integer.parseInt(st.nextToken());
          arr[a].add(b);
          arr[b].add(a);
      }
      //번호가 작은 것을 먼저 방문하기 위해 정렬
      for(int i=1;i<N+1;i++){
          Collections.sort(arr[i]);
      }
      visited = new boolean[N+1];
      dfs(V);
      System.out.println();
      visited = new boolean[N+1];
      bfs(V);
      
      br.close();
  }
  
  static void dfs(int node){
      System.out.print(node+" ");
      visited[node] = true;
      for(int i: arr[node]){
          if(!visited[i]){
              dfs(i);
          }
      }
  }
  
  static void bfs(int node){
      Queue<Integer> queue = new ArrayDeque<>();
      queue.add(node);
      visited[node]=true;
      
      while(!queue.isEmpty()){
          int v = queue.poll();
          System.out.print(v+" ");
          for(int i : arr[v]){
              if(!visited[i]){
                  visited[i]=true;
                  queue.add(i);
              }
          }
      }
  }
}