import java.io.*;
import java.util.*;

public class Main {
    
  public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      int N = Integer.parseInt(st.nextToken());
      int M = Integer.parseInt(st.nextToken());
      int K = Integer.parseInt(st.nextToken());
      
      int answer = 0;
      
      for(int i=0; i<N; i++){
          String row = br.readLine();
          String[] segments = row.split("1");
          
          for(String seg: segments){
              if(seg.length()>=K){
                  answer+=seg.length()-K+1;
              }
          }
      }
      
      System.out.println(answer);
      
      br.close();
  }
}