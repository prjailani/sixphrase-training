class Main {
    public static void main(String[] args) {
        int[] arr = {5,7,9,11,13,15};
        int n = 4;
        int l= arr.length;
        int[] res = new int[l];
        
        for(int i=0;i<l;i++){
            for(int j=1;j<=n;j++){
                res[i] += arr[(i+j)%l];
            }
        }
        for(int i:res){
            System.out.print(i+" ");
        }
    }
}