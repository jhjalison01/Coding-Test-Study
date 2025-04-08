import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      int N = Integer.parseInt(br.readLine());
      PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> {
          int first_abs = Math.abs(a);
          int second_abs = Math.abs(b);
          //절댓값이 같을 경우 작은 수 출력
          if (first_abs == second_abs){
              return a-b;
          }
          else{ // 절댓값 작은 수 출력
              return first_abs-second_abs;
          }
      });
      
      for (int i = 0;i<N;i++){
          int num = Integer.parseInt(br.readLine());
          
          if(num == 0){ //0이 나왔을 경우
              if(pq.isEmpty()) System.out.println(0); // 큐가 비었을 때 0 출력
              else System.out.println(pq.poll()); // 큐가 비어있지 않다면 조건에 맞는 숫자 출력 
          }else{
              pq.add(num);
          }
      }
      br.close();
  }
}