import java.util.*;

class Main{

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[] trees = new int[n];

        for(int i=0;i<n;i++){
            trees[i]=sc.nextInt();
        }
        
        int low=0;
        int high=1000000000;
        while(low<high){
            int mid = (low+high)/2;
            long sum=0;
            for(int t : trees){
                if(t>mid) sum+=t-mid;
            }
            if(sum>=m) low=mid+1;
            else high=mid;
        }
        System.out.println(low-1);
    }
        
}