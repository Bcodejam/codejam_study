// O(2^N)
import java.util.*;

class Main{
    static int n;
    static int s;
    static int answer = 0;
    static int[] arr=new int[20];
    static int check(int idx, int sum){
        if(idx>=n){
            if(sum==s) return 1;
            else return 0;
        }
        return check(idx+1, sum+arr[idx])+check(idx+1, sum);
    }
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        s = sc.nextInt();
        
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        
        answer=check(0,0);
        if(s==0) answer-=1;
        System.out.println(answer);
    }
}