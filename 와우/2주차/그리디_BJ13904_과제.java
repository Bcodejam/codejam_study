//O(N^2)
import java.util.*;

class Main{

    public static void main(String[] args){
        int answer=0;
        PriorityQueue<Integer>[] arr= new PriorityQueue[1001];
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        int maxd=0;
        for(int i=0;i<n;i++){
            int d=sc.nextInt();
            int w=sc.nextInt();
            if(arr[d]==null){
                arr[d]=new PriorityQueue<>(Collections.reverseOrder());
            }
            arr[d].add(w);
            maxd=Math.max(maxd,d);
        }
        
        for(int i=maxd;i>=1;i--){
            int maxw=0;
            int maxj=0;
            for(int j=i;j<=maxd;j++){
                if(arr[j]!=null && !arr[j].isEmpty() && arr[j].peek()>maxw) {
                    maxw=arr[j].peek();
                    maxj=j;
                }
            }
            answer+=maxw;
            if(maxj!=0)
                arr[maxj].remove();
        }
        System.out.println(answer);
    }
}