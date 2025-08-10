import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        //문제 개수
        int n = Integer.parseInt(st.nextToken());

        //난이도 별로 풀어야하는 문제 수
        st = new StringTokenizer(br.readLine());
        List<Integer> planProblems = new ArrayList<>();
        planProblems.add(0);
        for(int i = 0; i < 5; i++){
            planProblems.add(Integer.parseInt(st.nextToken()));
        }

        //해시맵 초기화
        Map<Integer, ArrayList<Integer>> problems = new HashMap<>();
        for(int i=1;i<=5;i++){
            problems.put(i, new ArrayList<>());
        }
        //문제 받기 - 난이도, 시간
        for(int i = 0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            int level = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());
            problems.get(level).add(time);
        }

        //최소 시간 계산
        int answer = 240; //다른 난이도 사이 쉬는 시간 총 시간
        for(int i=1;i<=5;i++){
            int cnt = planProblems.get(i); //난이도 별 풀 문제 개수
            List<Integer> timeList = problems.get(i);
            Collections.sort(timeList);

            answer+=timeList.get(0); // 항상 1문제 이상 품

            if(cnt>1){
                int beforeTime = timeList.get(0);
                for(int j = 1; j<cnt;j++){
                    int nowTime = timeList.get(j);
                    answer+=nowTime;
                    answer+=nowTime-beforeTime;
                    beforeTime=nowTime;
                }
            }
        }
        System.out.println(answer);
    }
}