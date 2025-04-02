import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException {
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(bf.readLine());
      
      int N = Integer.parseInt(st.nextToken());
      int[] arr = new int[N];
      for(int i=0;i<N;i++){
          st = new StringTokenizer(bf.readLine());
          arr[i]=Integer.parseInt(st.nextToken());
      }
      
      Deque<Integer> stack = new ArrayDeque<>();
      StringBuffer answer = new StringBuffer();
      int num = 1; //오름차순 수
      boolean result = true;
      for(int i=0;i<arr.length;i++){
          int su = arr[i]; //현재 수열의 수
          if(su>=num){
              while(su>=num){
                  stack.push(num++);
                  answer.append("+\n");
              }
              stack.pop();
              answer.append("-\n");
          }else{ //현재 수열 값 < 오름차순 자연수
              int n = stack.pop();
              if(n>su){
                  System.out.println("NO");
                  result = false;
                  break;
              } else{
                  answer.append("-\n");
              }
          }
      }
      if (result) System.out.println(answer.toString());
      bf.close();
  }
}