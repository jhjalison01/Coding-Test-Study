import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException {
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(bf.readLine());
      
      int n = Integer.parseInt(st.nextToken());
      
      //숫자 저장하기
      int arr[] = new int[n];
      st = new StringTokenizer(bf.readLine());
      for (int i = 0; i<n; i++){
          arr[i]=Integer.parseInt(st.nextToken());
      }
      //숫자 정렬
      Arrays.sort(arr);
      
      int cnt=0;
      for(int k = 0;k<n;k++){
          long find = arr[k];
          int start=0;
          int end=n-1;
          while(start<end){
              //더하는 두 숫자가 find가 아니어야 함
              if(start==k || end==k){
                  if (start==k) start++;
                  else if (end==k) end--;
              }else{
                  //더한 값이 find일 경우
                  if(arr[start]+arr[end]==find){
                      cnt++;
                      break;
                  }else if (arr[start]+arr[end]<find){
                      start++;
                  }else{
                      end--;
                  }
              }
          }
      }
      System.out.println(cnt);
      bf.close();
  }
}