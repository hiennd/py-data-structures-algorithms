import java.util.HashMap;
import java.util.Map;
public class ArrayMostFreq {
    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        // mostFrequent(array1) should return 1.
        int[] array1 = {1, 3, 1, 3, 2, 1};
        if (ArrayMostFreq.mostFreqent(array1) == 1) {
            System.out.printf("Correct! ArrayMostFreq.mostFreqent(array1)=%d", ArrayMostFreq.mostFreqent(array1) );
        }
        // mostFrequent(array2) should return 3.
        int[] array2 = {3, 3, 1, 3, 2, 1};
        // mostFrequent(array3) should return null.
        int[] array3 = {};
        // mostFrequent(array4) should return 0.
        int[] array4 = {0};
        // mostFrequent(array5) should return -1.
        int[] array5 = {0, -1, 10, 10, -1, 10, -1, -1, -1, 1};
    }
    // Implement your solution below.
    public static Integer mostFreqent(int[] arr) {
        Integer maxItem = null;
        Integer max = 0;
        HashMap<Integer, Integer> histogram = new HashMap<Integer, Integer>();
        for (int num : arr) {
            histogram.compute(num, (k, value) -> value == null ? 0 : value + 1);
            // histogram.put(num, histogram.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> e : histogram.entrySet()) {
            if (e.getValue() >= max) {
                max = e.getValue();
                maxItem = e.getKey();
            };
        };
        return maxItem;
    }
}
