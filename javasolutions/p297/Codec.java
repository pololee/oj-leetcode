/**
 https://leetcode.com/problems/serialize-and-deserialize-binary-tree/#/description
 */

package javasolutions.p297;

import javasolutions.TreeNode;
import java.util.Queue;
import java.util.LinkedList;

public class Codec {

  public String serialize(TreeNode root) {
    if(root == null) return null;

    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);
    StringBuilder answer = new StringBuilder();

    while(!queue.isEmpty()) {
      TreeNode pointer = queue.poll();
      if(pointer != null) {
        answer.append(String.format("%d,", pointer.val));
        queue.add(pointer.left);
        queue.add(pointer.right);
      } else {
        answer.append("#,");
      }
    }

    return answer.substring(0, answer.length() - 1).toString();
  }

  public TreeNode deserialize(String data) {
    if(data == null || data.isEmpty()) return null;

    String[] valueStrs = data.split(",");
    TreeNode root = new TreeNode(Integer.parseInt(valueStrs[0]));
    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);

    for(int i = 1; i < valueStrs.length; i++) {
      TreeNode pointer = queue.poll();

      if(!valueStrs[i].equals("#")) {
        pointer.left = new TreeNode(Integer.parseInt(valueStrs[i]));
        queue.add(pointer.left);
      }

      i++;
      if(!valueStrs[i].equals("#")) {
        pointer.right = new TreeNode(Integer.parseInt(valueStrs[i]));
        queue.add(pointer.right);
      }
    }

    return root;
  }

  public static void main(String[] args) {
    TreeNode test = TreeNode.dummyTree();
    Codec cal = new Codec();

    String encodedString = cal.serialize(test);
    System.out.println(encodedString);
    System.out.println(cal.serialize(cal.deserialize(encodedString)));

    TreeNode test2 = new TreeNode(-1);
    test2.left = new TreeNode(0);
    test2.right = new TreeNode(1);
    String answer = cal.serialize(test2);
    System.out.println(answer);
    System.out.println(cal.serialize(cal.deserialize(answer)));
  }
}