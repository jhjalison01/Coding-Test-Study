import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int nums[] = new int[n];
      for(int i = 0; i<n ;i++){
          nums[i] = sc.nextInt();
      }
      long sum = 0;
      long max = 0;
      for(int i=0; i<n;i++){
          if (nums[i]>max) max = nums[i];
          sum=sum+nums[i];
      }
      System.out.println(sum*100.0/max/n);
  }
}