package javasolutions.p39;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class CombinationSum {
  public List<List<Integer>> combinationSum(int[] candidates, int target) {
    List<List<Integer>> results = new ArrayList<>();

    Arrays.sort(candidates);
    List<Integer> oneResult = new ArrayList<>();
    combinationSumDFS(candidates, 0, target, oneResult, results);

    return results;
  }

  private void combinationSumDFS(int[] candidates, int start, int target, List<Integer> oneResult, List<List<Integer>> results) {
    if ( target < 0) {
      return;
    } else if (target == 0) {
      results.add(new ArrayList<Integer>(oneResult));
      return;
    } else {
      for (int i = start; i < candidates.length; i++) {
        oneResult.add(candidates[i]);
        combinationSumDFS(candidates, i, target - candidates[i], oneResult, results);
        oneResult.remove(oneResult.size() - 1);
      }
    }
  }

  public static void main(String[] args) {
    int[] test = {2,3,6,7};
    CombinationSum cal = new CombinationSum();

    List<List<Integer>> ans = cal.combinationSum(test, 7);

    for (List<Integer> list : ans) {
      System.out.println(Arrays.toString(list.toArray()));
    }
  }
}