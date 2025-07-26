class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for(int i=0; i<n;i++){
            int mapOneNum = arr1[i];
            int mapTwoNum = arr2[i];
            
            //이진수로 바꾸기
            String oneBinary = toBinary(mapOneNum,n);
            String twoBinary = toBinary(mapTwoNum,n);
            //지도 1,2 합치기
            String row = "";
            for(int j=0;j<n;j++){
                
                if(oneBinary.charAt(j)=='0' && twoBinary.charAt(j)=='0'){
                    row+=" ";
                }else{
                    row+="#";
                }
            }
            answer[i]=row;
        }
        return answer;
    }
    
    public String toBinary(int num,int cnt){
        String result = "";
        
        while(num>=1){
            if(num==1){
                result='1'+result;
                cnt-=1;
                break;
            }
            
            result=Integer.toString(num%2)+result;
            num = num/2;
            cnt-=1;
        }
        result = "0".repeat(cnt)+result;
        return result;
    }
}