import java.util.*;

class Main{
    static int n;
    static int s;
    static int answer = 0;
    static int[] arr=new int[20];
    static void check(int idx, int cnt, int size, int sum){
        if(cnt>=size){
            if(sum==s) answer++;
            return;
        }
        if(idx>=n) return;
        for(int i=idx;i<n;i++){
            check(i+1, cnt+1, size, sum+arr[i]);
        }
    }
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        s = sc.nextInt();
        
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        
        for(int size=1;size<=n;size++){
            for(int i=0;i<=n-size;i++){
                check(i+1, 1, size, arr[i]);
            }
        }

        System.out.println(answer);
    }
}