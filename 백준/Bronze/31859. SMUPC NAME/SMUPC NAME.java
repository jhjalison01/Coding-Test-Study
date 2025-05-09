import java.io.*;
import java.util.*;

public class Main {
    
  public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      int num = Integer.parseInt(st.nextToken());
      String name = st.nextToken();
      
      //1. 중복 없애기
      StringBuilder temp = new StringBuilder();
      StringBuilder duplicateChars = new StringBuilder();
      for(int i=0; i<name.length(); i++){
          char ch = name.charAt(i);
          String chStr = String.valueOf(ch);
          if(temp.toString().contains(chStr)){
              duplicateChars.append(ch);
          }else{
              temp.append(ch);
          }
      }
      //2. 맨 뒤에 버려진 문자의 총개수 + 4 붙이기
      temp.append(duplicateChars.length()+4);
      //3. 맨 앞에 출전 등록 번호 + 1906 붙이기
      temp.insert(0,(num+1906));
      //4.문자열 뒤집기
      temp.reverse();
      //5. 맨 앞에 smupc_ 붙이기
      temp.insert(0,"smupc_");
      
      System.out.println(temp);
      br.close();
  }
  
  
}