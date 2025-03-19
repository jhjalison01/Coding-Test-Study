import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    
    int cnt = 1;
    int start = 1;
    int end = 1;
    int sum=1; //숫자 n을 뽑는 경우 1
    
    while(end!=n){
        if(sum==n){
            cnt++;
            end++;
            sum = sum+end;
        }else if(sum>n){
            sum=sum-start;
            start++;
        }else{
            end++;
            sum=sum+end;
        }
    }
    System.out.println(cnt);
  }
}