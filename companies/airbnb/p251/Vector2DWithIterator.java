package airbnb.p251;

import java.util.List;
import java.util.Iterator;

public class Vector2DWithIterator implements Iterator<Integer> {
  private Iterator<List<Integer>> rowIterator;
  private Iterator<Integer> colIterator;

  public Vector2DWithIterator(List<List<Integer>> vec2d) {
    rowIterator = vec2d.iterator();
    colIterator = null;
  }

  @Override
  public Integer next() {
    return colIterator.next();
  }

  @Override
  public boolean hasNext() {
    while((colIterator == null || !colIterator.hasNext()) && rowIterator.hasNext()) {
      colIterator = rowIterator.next().iterator();
    }

    return colIterator != null && colIterator.hasNext();
  }
}