import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        //n개의 문제, m명의 이용자
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        StringBuilder answerList = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        //각 문제의 난이도
        int[] problemLevel = new int[n];
        for(int i = 0;i<n;i++){
            problemLevel[i] = Integer.parseInt(st.nextToken());
        }

        //문제 난이도 내림차순으로 정렬
        Arrays.sort(problemLevel);
        int problemNum = problemLevel.length;

        //크기 k에 대한 문제의 수
        List<Integer> kProblems = new ArrayList<>();
        kProblems.add(0);
        for(int k = 1; 3*k*(k-1)+1<=problemNum; k++){
            kProblems.add(3*k*(k-1)+1);
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0;i<m;i++){
            int problemSolveNum;
            int userLevel = Integer.parseInt(st.nextToken());

            problemSolveNum = upperBound(problemLevel,userLevel);

            int kIndex = Collections.binarySearch(kProblems, problemSolveNum);
            if(kIndex>=0){
                answerList.append(kIndex).append(" ");
            }else{
                answerList.append(-kIndex-2).append(" ");
            }
        }

        //이용자가 해결할 수 있는 문제로만 이루어진 가장 큰 게임판의 크기
        System.out.println(answerList.toString().trim());
    }

    // upperBound: 배열에서 value 이하 원소 개수
    static int upperBound(int[] arr, int value) {
        int left = 0;
        int right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] <= value){
                left = mid + 1;
            } 
            else right = mid;
        }
        return left; // value인 원소 개수
    }
}

