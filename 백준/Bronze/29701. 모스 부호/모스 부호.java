import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Map<String,String> map = new HashMap<>();
        map.put(".-","A");
        map.put("-...","B");
        map.put("-.-.","C");
        map.put("-..","D");
        map.put(".","E");
        map.put("..-.","F");
        map.put("--.","G");
        map.put("....","H");
        map.put("..","I");
        map.put(".---","J");
        map.put("-.-","K");
        map.put(".-..","L");
        map.put("--","M");
        map.put("-.","N");
        map.put("---","O");
        map.put(".--.","P");
        map.put("--.-","Q");
        map.put(".-.","R");
        map.put("...","S");
        map.put("-","T");
        map.put("..-","U");
        map.put("...-","V");
        map.put(".--","W");
        map.put("-..-","X");
        map.put("-.--","Y");
        map.put("--..","Z");
        map.put(".----","1");
        map.put("..---","2");
        map.put("...--","3");
        map.put("....-","4");
        map.put(".....","5");
        map.put("-....","6");
        map.put("--...","7");
        map.put("---..","8");
        map.put("----.","9");
        map.put("-----","0");
        map.put("--..--",",");
        map.put(".-.-.-",".");
        map.put("..--..","?");
        map.put("---...",":");
        map.put("-....-","-");
        map.put(".--.-.","@");

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder answer = new StringBuilder();
        for(int i=0;i<N;i++){
            String code = st.nextToken();
            answer.append(map.get(code));
        }
        System.out.println(answer);

        br.close();
    }
}