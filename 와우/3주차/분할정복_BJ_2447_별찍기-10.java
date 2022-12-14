import java.util.*;

class Main{
    static char[][] answer = new char[6561][6561];
    static void f(int x, int y, int n){
        if(n==1){
            answer[y][x]='*';
            return;
        }
        
        for(int i=0; i<n; i+=n/3){
            for(int j=0; j<n;j+=n/3){
                if(j==n/3 && i==n/3){
                    for(int k=0;k<n/3;k++){
                        for(int l=0;l<n/3;l++){
                            answer[y+i+k][x+j+l]=' ';
                        }
                    }
                    continue;
                }
                f(x+j,y+i,n/3);
            }
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();
        int n = sc.nextInt();

        f(0,0,n);

        for(int i=0;i<n;i++) {
          for(int j=0;j<n;j++) {
            sb.append(answer[i][j]);
          }
          sb.append("\n");
        }
        System.out.println(sb);
    }
}