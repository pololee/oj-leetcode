/**
 * https://leetcode.com/problems/flatten-2d-vector/#/description
 * 
 * Implement an iterator to flatten a 2d vector.
 * For example,
 * Given 2d vector =
 * [
 *  [1,2],
 *  [3],
 *  [4,5,6]
 * ]
 * By calling next repeatedly until hasNext returns false, 
 * the order of elements returned by next should be: [1,2,3,4,5,6].
 */

package airbnb.p251;

import java.util.Iterator;
import java.util.List;

public class Vector2D implements Iterator<Integer> {
  private List<List<Integer>> vec2d;
  private int rowIdx;
  private int colIdx;

  public Vector2D(List<List<Integer>> vec2d) {
    this.vec2d = vec2d;
    rowIdx = 0;
    colIdx = 0;
  }

  @Override
  public Integer next() {
    return vec2d.get(rowIdx).get(colIdx);
    colIdx++;
  }

  @Override
  public boolean hasNext() {
    // why we need while?
    // because the vec2d could have empty rows in it.
    while(rowIdx < vec2d.size() && colIdx == vec2d.get(rowIdx).size()) {
      rowIdx++;
      colIdx = 0;
    }

    return rowIdx < vec2d.size();
  }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i = new Vector2D(vec2d);
 * while (i.hasNext()) v[f()] = i.next();
 */

