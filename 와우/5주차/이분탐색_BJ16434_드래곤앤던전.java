import java.util.*;

class Main{

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] d = new int[n][3];
        long attack = sc.nextInt();

        for(int i=0;i<n;i++){
            d[i][0]  = sc.nextInt();
            d[i][1] = sc.nextInt();
            d[i][2]= sc.nextInt();
        }
        long lo=0;
        long hi=Long.MAX_VALUE;
        
        while(lo<hi){
            long mid=(lo+hi)/2;
            long curr_attack=attack;
            long hp=mid;
            boolean alive=true;
            for(int i=0;i<n;i++){
                if(d[i][0]==1){
                    hp-= (d[i][2]%curr_attack==0? d[i][2]/curr_attack-1: d[i][2]/curr_attack)*d[i][1];
                    if(hp<=0) {
                        alive=false;
                        break;
                    }
                }else{
                    curr_attack+=d[i][1];
                    if(hp+d[i][2]<=mid) hp+=d[i][2];
                    else hp=mid;
                }
            }
            if(!alive)lo=mid+1;
            else hi=mid;
        }
        
        System.out.println(lo);
    }
        
}