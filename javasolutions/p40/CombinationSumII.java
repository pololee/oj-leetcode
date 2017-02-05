package javasolutions.p40;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class CombinationSumII {
  public List<List<Integer>> combinationSum2(int[] candidates, int target) {
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
        if (i > start && candidates[i] == candidates[i-1]) continue;
        oneResult.add(candidates[i]);
        combinationSumDFS(candidates, i + 1, target - candidates[i], oneResult, results);
        oneResult.remove(oneResult.size() - 1);
      }
    }
  }

  public static void main(String[] args) {
    int[] test = {10, 1, 2, 7, 6, 1, 5};
    CombinationSumII cal = new CombinationSumII();

    List<List<Integer>> ans = cal.combinationSum2(test, 8);

    for (List<Integer> list : ans) {
      System.out.println(Arrays.toString(list.toArray()));
    }
  }
}