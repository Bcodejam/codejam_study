// O(4^(log_2_N))
import java.util.*;

class Main{
    static int[][] arr = new int[64][64]; 
    static String f(int x, int y, int n){
        if(n==1){
            return Integer.toString(arr[y][x]);
        }
        String a=f(x,y,n/2);
        String b=f(x+n/2,y,n/2);
        String c=f(x,y+n/2,n/2);
        String d=f(x+n/2,y+n/2,n/2);
        if(a.equals(b) && b.equals(c) && c.equals(d) && a.length()==1){
            return a;
        }
        return "("+a+b+c+d+")";
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        for(int i=0;i<n;i++){
            String tmp = sc.next();
            for(int j=0;j<n;j++){
                arr[i][j]=Integer.valueOf(tmp.substring(j,j+1));
            }
        }
        System.out.println(f(0,0,n));
    }
}