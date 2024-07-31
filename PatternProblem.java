import java.util.Scanner;
class test{
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();sc.close();
        String star="*",space="  ".repeat(n-1);
        for(int i=0;i<=n*2;i++,star=(i<=n)?star+"*":star.substring(0,star.length()-1),space=(i<=n+1)?space.replaceFirst("  ",""):space+"  ")
            if(i!=n)System.out.println(star+space+star);
    }
}