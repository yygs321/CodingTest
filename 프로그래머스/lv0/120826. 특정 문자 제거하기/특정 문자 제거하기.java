class Solution {
    public String solution(String my_string, String letter) {
        StringBuilder sb= new StringBuilder();
        String[] sa=my_string.split("");
        for(String s:sa){
            if(s.equals(letter)){
                continue;
            }
            sb.append(s);
        }
        return sb.toString();
    }
}