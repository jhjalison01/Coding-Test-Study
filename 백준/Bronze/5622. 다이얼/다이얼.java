import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String words = br.readLine();

        int[] time = {
                3,3,3,
                4,4,4,
                5,5,5,
                6,6,6,
                7,7,7,
                8,8,8,8,
                9,9,9,
                10,10,10,10
        };

        int cnt = 0;
        for(int i = 0; i < words.length(); i++) {
            char w = words.charAt(i);
            cnt+=time[w-'A'];
        }

        //다이얼 걸기 위해서 필요한 최소 시간
        System.out.println(cnt);
    }
}