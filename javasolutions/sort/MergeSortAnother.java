package javasolutions.sort;

public class MergeSortAnother {
  public int[] mergeSort(int[] nums) {
    int length = nums.length;

    if(length == 1) return nums;

    int[] a = new int[length/2];
    for (int i=0; i<a.length; i++) {
      a[i] = nums[i];
    }

    int[] b = new int[length - length/2];
    for (int i=0; i<b.length; i++) {
      b[i] = nums[i + length/2];
    }

    return merge(mergeSort(a), mergeSort(b));
  }

  private int[] merge(int[] a, int[] b) {
    int[] result = new int[a.length + b.length];

    int aIdx=0, bIdx=0, index = 0;

    while(aIdx < a.length && bIdx < b.length) {
      if(a[aIdx] < b[bIdx]) {
        result[index] = a[aIdx];
        aIdx++;
      } else {
        result[index] = b[bIdx];
        bIdx++;
      }

      index++;
    }

    while(aIdx < a.length) {
      result[index] = a[aIdx];
      index++;
      aIdx++;
    }

    while(bIdx < b.length) {
      result[index] = b[bIdx];
      index++;
      bIdx++;
    }

    return result;
  }

  public void print(int[] nums) {
    System.out.print(nums[0]);

    for (int i=1; i<nums.length; i++) {
      System.out.format(", %d", nums[i]);
    }

    System.out.println();
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    MergeSortAnother cal = new MergeSortAnother();
    test = cal.mergeSort(test);

    cal.print(test);
  }
}