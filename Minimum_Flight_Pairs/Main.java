public class Main {
    public static void main(String[] args) {
        int[] flight_times = {120,90,110,95,120,90};
        int min = flight_times[0];
        for(int i:flight_times){
            if(i<min){
                min=i;
            }
        }
        System.out.println("Minimum = "+min);
        
        for(int i=0;i<flight_times.length;i++){
            for(int j=i+1;j<flight_times.length;j++){
                if(flight_times[i]==min && flight_times[j]==min){
                    System.out.println(i+" "+j);
                }
            }
        }
    }
}