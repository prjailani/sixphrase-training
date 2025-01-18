import java.util.*;

class Main {
    public static void main(String[] args) {

        HashMap<Integer, String> number = new HashMap<>();
        number.put(0,"Zero");
        number.put(1,"One");
        number.put(2,"Two");
        number.put(3,"Three");
        number.put(4,"Four");
        number.put(5,"Five");
        number.put(6,"Six");
        number.put(7,"Seven");
        number.put(8,"Eight");
        number.put(9,"Nine");
        
        String ans = "";
        long n = 9986438886L;
        int d = 9;
        while(d>=0){
            int count=1;
            int prev = (int)(n/(Math.pow(10,d))%10);
            d--;
            while(d>0 && (((int)(n/(Math.pow(10,d)))%10))==prev){
                count++;
                d--;
            }
            while(count>0){
                if (count==1){
                    ans += number.get(prev)+" ";
                    count--;
                }
                else if (count==2){
                    ans += "double "+number.get(prev)+" ";
                    count-=2;
                }
                else if(count==4){
                    ans += "double "+number.get(prev)+" double "+number.get(prev)+" ";
                    count-=4;
                }
                else{
                    ans += "triple "+ number.get(prev)+" ";
                    count -= 3;
                }
            }
            
        }
        System.out.println(ans);
    }
}