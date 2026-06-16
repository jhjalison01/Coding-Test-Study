class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int small = 0;
        int big = 0;
        
        for(int i=0; i<sizes.length;i++){
            int a = sizes[i][0];
            int b = sizes[i][1];
            
            small = Math.max(small, Math.min(a,b));
            big = Math.max(big, Math.max(a,b));
        }
        
        answer = small * big;
        
        return answer;
    }
}