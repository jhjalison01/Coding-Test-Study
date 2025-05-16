import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); // 출력 모으기

        int T = Integer.parseInt(br.readLine());

        for(int i = 0; i < T; i++) {
            long N = Long.parseLong(br.readLine());

            //몇 층인지
            int floor = Long.toBinaryString(N).length();
            //왼쪽에서 몇번째인지
            long num = N - (1L << (floor - 1)) + 1;

            while(floor>0){
                String numStr = Long.toString(num);
                if (numStr.length()<18){
                    sb.append(floor)
                            .append("0".repeat(18 - numStr.length()))
                            .append(numStr)
                            .append("\n");
                }
                else{
                    sb.append(floor).append(numStr).append("\n");
                }
                floor--;
                num = (num+1)/2;
            }
        }
        System.out.println(sb);
    }
}