import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        //초코바 개수
        int n = Integer.parseInt(st.nextToken());

        int answerShort = 0;
        int answerLong = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int shortLength = Integer.parseInt(st.nextToken());
            int longLength = Integer.parseInt(st.nextToken());

            if(shortLength > longLength){
                int temp = shortLength;
                shortLength = longLength;
                longLength = temp;
            }

            answerShort = Math.max(answerShort, shortLength);
            answerLong = Math.max(answerLong, longLength);
        }

        //모든 초코바를 굳힐 수 있는 틀의 최소 면적
        System.out.println((long)answerShort*answerLong);
    }
}