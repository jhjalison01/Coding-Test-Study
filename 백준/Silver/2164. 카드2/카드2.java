import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException {
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(bf.readLine());
      
      int N = Integer.parseInt(st.nextToken());
      
      //큐에 숫자 넣기기
      Deque<Integer> queue = new LinkedList<>();
      for(int i = 1;i<N+1;i++){
          queue.add(i);
      }
      
      while(queue.size() > 1){
          queue.removeFirst(); // 제일 위에 있는 카드 버리기
          int num = queue.removeFirst(); //제일 위에 있는 카드 추출출
          queue.add(num); //맨 뒤에 숫자 넣기기
      }
      System.out.println(queue.remove()); // 마지막 숫자 프린트트
      bf.close();
  }
}