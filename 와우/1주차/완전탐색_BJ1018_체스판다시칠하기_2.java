import java.util.*;

class Main{
   static int answer = Integer.MAX_VALUE;
   static int n;
   static int m;
   static List<char[]> list = new ArrayList<>();

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        
        for(int y=0;y<n;y++){
            String s = sc.next();
            list.add(s.toCharArray());
        }

        for(int starty=0;starty<=n-8;starty++){
            for(int startx=0;startx<=m-8;startx++){
                int cnt1=0;int cnt2=0;
                for(int y=starty;y<starty+8;y++){
                    for(int x=startx;x<startx+8;x++){
                        if((x+y)%2==0){
                            if(list.get(y)[x]=='W') cnt1++;
                            else cnt2++;
                        }else{
                            if(list.get(y)[x]=='B') cnt1++;
                            else cnt2++;
                        }
                    }
                }
                answer=Math.min(cnt1,answer);
                answer=Math.min(cnt2,answer);
            }
        }
        System.out.println(answer);
    }
}