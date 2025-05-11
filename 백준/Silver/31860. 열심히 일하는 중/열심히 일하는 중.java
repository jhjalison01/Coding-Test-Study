import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // N개의 일
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken()); //중요도가 K 이하가 되면 그 일은 완료

        PriorityQueue<Integer> works = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0; i < N; i++) {
            works.add(Integer.parseInt(br.readLine()));
        }

        int ySatisfaction = 0;
        int days =0;
        StringBuilder satisfactions = new StringBuilder();

        while(!works.isEmpty()) {
            days++;
            int todayImportance = works.poll(); //중요도가 높은 순으로 일함
            int tSatisfaction = ySatisfaction / 2+todayImportance; //오늘 만족감 계산
            satisfactions.append(tSatisfaction).append('\n');
            ySatisfaction = tSatisfaction;
            todayImportance -=M; //일을 처리한 후 중요도 M만큼 감소
            if(todayImportance > K) //중요도가 K 이하가 되면 그 일은 완료
                works.add(todayImportance);
        }
        //출력
        bw.write(days+"\n");
        bw.write(satisfactions.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}