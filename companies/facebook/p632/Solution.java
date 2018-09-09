class Solution {
   class Node{
       int group;
       int value;
       public Node(int group, int value){
           this.group = group;
           this.value = value;
       }
   }
   public int[] smallestRange(List<List<Integer>> nums) {
       if (nums == null || nums.size() == 0){
           return new int[0];
       }

       int k = nums.size();
       List<Node> list = new ArrayList<>();
       for (int i = 0; i < nums.size(); i++){
           for (int j = 0; j < nums.get(i).size(); j++){
               list.add(new Node(i, nums.get(i).get(j)));
           }
       }

       Collections.sort(list, (Node a, Node b) -> (a.value - b.value));

       Map<Integer, Integer> map = new HashMap<>();
       int diff = Integer.MAX_VALUE;
       int j = 0;
       int[] res = new int[2];

       for (int i = 0; i < list.size(); i++){
           while (j < list.size() && map.size() < k){
               Node tmp = list.get(j);
               if (!map.containsKey(tmp.group)){
                   map.put(tmp.group, 0);
               }
               map.put(tmp.group, map.get(tmp.group) + 1);
               j ++;
           }

           if (map.size() == k){
               if (list.get(j - 1).value - list.get(i).value < diff){
                   diff = list.get(j - 1).value - list.get(i).value;
                   res[0] = list.get(i).value;
                   res[1] = list.get(j - 1).value;
               }
           }

           if (map.get(list.get(i).group) == 1){
               map.remove(list.get(i).group);
           }
           else{
               map.put(list.get(i).group, map.get(list.get(i).group) - 1);
           }
       }

       return res;

   }
}
