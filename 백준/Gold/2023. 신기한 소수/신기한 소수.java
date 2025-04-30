import java.io.*;
import java.util.*;

public class Main {
  static int N;
  public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      N = Integer.parseInt(br.readLine());
      //소수 2, 3, 5, 7로 탐색 시작
      dfs(1, 2);
      dfs(1, 3);
      dfs(1, 5);
      dfs(1, 7);
      
      br.close();
  }
  
  static void dfs(int depth, int number){
      if(depth == N){
          if(isPrime(number)){
              System.out.println(number);
          }
          return;
      }
      for(int i = 1;i<10;i++){
          //짝수일 경우 탐색할 필요 없음
          if(i%2 == 0){
              continue;
          }
          if(isPrime(number*10+i)){
              dfs(depth+1,number*10+i);
          }
      }
  }
  
  static boolean isPrime(int num){
      for(int i = 2;i<=num/2;i++){
          if(num%i==0) return false;
      }
      return true;
  }
}