import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    //재료 개수, M 입력 받기기
    int n = Integer.parseInt(bf.readLine());
    int m = Integer.parseInt(bf.readLine());
    //재료 번호 입력 받기
    int[] arr = new int[n];
    StringTokenizer st = new StringTokenizer(bf.readLine());
    for(int i=0;i<n;i++){
        arr[i]=Integer.parseInt(st.nextToken());
    }
    //번호 정렬
    Arrays.sort(arr);
    
    int cnt=0;
    int start=0;
    int end = n-1;
    
    while(start<end){
        if (arr[start]+arr[end]<m){
            start++;
        }else if(arr[start]+arr[end]>m){
            end--;
        }else{
            cnt++;
            start++;
            end--;
        }
    }
    System.out.println(cnt);
    bf.close();
  }
}