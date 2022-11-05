import java.util.*;

class Main{
   static int answer = Integer.MAX_VALUE;
   static int n;
   static int m;
   static List<char[]> list = new ArrayList<>();

   static void check(char ybefore){
       for(int starty=0;starty<=n-8;starty++){
            for(int startx=0;startx<=m-8;startx++){
                int cnt=0;
                for(int y=starty;y<starty+8;y++){
                    char[] carr = list.get(y);
                    char xbefore=' ';
                    for(int x=startx;x<startx+8;x++){
                        if(x==startx){
                            if(carr[x]==ybefore){
                                cnt++;
                                xbefore=carr[x]=='B'?'W':'B';
                            }else{
                                xbefore=carr[x]=='B'?'B':'W';
                            }
                            ybefore=ybefore=='B'?'W':'B';
                        }
                        else if(carr[x]==xbefore){
                            cnt++;
                            xbefore=carr[x]=='B'?'W':'B';

                        }else{
                            xbefore=carr[x]=='B'?'B':'W';
                        }
                    }
                }
                answer=Math.min(answer,cnt);
            }
        }
   }
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        
        for(int y=0;y<n;y++){
            String s = sc.next();
            list.add(s.toCharArray());
        }

        check('B');
        check('W');
        System.out.println(answer);
    }
}