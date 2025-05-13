import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); //팀의 수
        int M = Integer.parseInt(st.nextToken()); // 경기의 수
        int K = Integer.parseInt(st.nextToken()); //팀번호

        int[] score = new int[N+1];
        List<int[]> undecidedMatches = new ArrayList<>(); //미정 경기
        Set<Integer> involvedTeams = new HashSet<>(); // 미정 경기 참여 팀

        //각 팀의 기본 점수 저장, 미정 경기 저장
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int team1 = Integer.parseInt(st.nextToken());
            int team2 = Integer.parseInt(st.nextToken());
            int result = Integer.parseInt(st.nextToken());

            if(result == 1){
                score[team1]++;
            }else if(result == 2){
                score[team2]++;
            }else{
                undecidedMatches.add(new int[]{team1, team2});
                involvedTeams.add(team1);
                involvedTeams.add(team2);
            }
        }

        // 응원팀도 점수 비교에 포함시켜야 하므로 추가
        involvedTeams.add(K);

        //미정 경기 완전 탐색 - 비스마스킹
        int U = undecidedMatches.size();
        int answer = 0;

        // involved 팀들만 복사하는 base map
        Map<Integer, Integer> baseScoreMap = new HashMap<>();
        for (int t : involvedTeams) {
            baseScoreMap.put(t, score[t]);
        }

        for(int mask = 0; mask<(1<<U); mask++){
            // tempScoreMap을 base에서 복사
            Map<Integer, Integer> tempScore = new HashMap<>(baseScoreMap);

            for(int i=0; i<U; i++){
                int[] match = undecidedMatches.get(i);
                // i번째 비트가 꺼져 있을 경우 팀 1 승리, 비트가 켜져 있으면 팀 2 승리
                int winner = ((mask & (1<<i)) == 0) ? match[0] : match[1];
                tempScore.put(winner, tempScore.getOrDefault(winner, 0) + 1);
            }

            //K팀이 단독 1위를 할 경우 저장
            boolean isTop = true;
            for(int t: involvedTeams){
                if(t != K && tempScore.get(t) >= tempScore.get(K)){
                    isTop = false;
                    break;
                }
            }

            if(isTop){
                answer++;
            }
        }

        System.out.println(answer);
        br.close();
    }
}