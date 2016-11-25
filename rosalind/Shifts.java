public class Shifts{

    public static void getElementSwaps(int[] ar, int size) {
        //base case
        if (size <= 1) {
            return 
        }
        int shifts = 0;
        //starting at 2nd element as first element is already sorted.
        //Loop Invariant - left part of the array is already sorted.
        for (int i = 1; i < size; i++) {
            int moveMe = ar[i];
            int j = i;
            while (j > 0 && moveMe < ar[j - 1]) {
                //Move element
                ar[j] = ar[j - 1];
                --j;
                //increase the count as element swap is happend
                ++shifts;
            }
            ar[j] = moveMe;
        }
        System.out.println(shifts);
    }


    public static void main(String[] argv){
      
        int[] ar = {1,2,3,4,5,2,10,9};
        getElementSwaps(ar,8);
    }


}
