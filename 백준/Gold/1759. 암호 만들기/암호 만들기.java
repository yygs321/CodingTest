import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N,C, moflag, zaflag;
    static String[] str, result;
    static ArrayList<String> mo=new ArrayList<>(Arrays.asList("a","e","i","o","u"));

    public static void main(String[] args) throws IOException {
        //최소 1개의모음 , 최소 2개의 자음
        //알파벳 오름차순 정렬

        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        //암호: 서로다른 C개의 문자 중 N개로 구성(조합)
        N=Integer.parseInt(st.nextToken());
        C=Integer.parseInt(st.nextToken());

        str=new String[C];
        result=new String[N];

        st=new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            str[i]=st.nextToken();
        }
        //오름차순 정렬
        Arrays.sort(str);
        combi(0,0);

    }
    private static void combi(int cnt, int start){
        if(cnt==N){
            moflag=0;
            zaflag=0;
            String answer="";
            for (String a: result) {
                answer+=a;
                if(mo.contains(a)) moflag++;
                else zaflag++;
            }
            //4글자 중 모음 최소 1개, 자음 최소 2개이므로 0<모음<=2
            if (moflag>=1 && zaflag>=2){
                System.out.print(answer);
                System.out.println();
            }
            return;
        }

        for (int i = start; i < C; i++) {
            result[cnt]=str[i];
            combi(cnt+1,i+1);
        }
    }
}