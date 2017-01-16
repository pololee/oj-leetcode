package javasolutions.p447;

import java.util.Map;
import java.util.HashMap;

public class NumberOfBoomerangs {
  public int numberOfBoomerangs(int[][] points) {
    if(points.length == 0 || points[0].length == 0) return 0;

    int result = 0;

    for (int i=0; i<points.length; i++) {
      Map<Integer, Integer> map = new HashMap<>();

      for (int j=0; j<points.length; j++) {
        int x = points[j][0] - points[i][0];
        int y = points[j][1] - points[i][1];

        int distanceSquare = x * x + y * y;
        System.out.format("distanceSquare %d \n", distanceSquare);

        if (map.containsKey(distanceSquare)) {
          map.put(distanceSquare, map.get(distanceSquare) + 1);
        } else {
          map.put(distanceSquare, 1);
        }
      }

      for (Integer distance : map.keySet()) {
        int numberOfPointsWithSuchDistance = map.get(distance);
        System.out.format("numberOfPointsWithSuchDistance %d \n", numberOfPointsWithSuchDistance);
        result += numberOfPointsWithSuchDistance * (numberOfPointsWithSuchDistance - 1);
      }
    }

    return result;
  }

  public static void main(String[] args) {
    int[][] points = new int[][]{
      {1, 1},
      {1, 2}
    };

    NumberOfBoomerangs cal = new NumberOfBoomerangs();
    System.out.println(cal.numberOfBoomerangs(points));
  }
}