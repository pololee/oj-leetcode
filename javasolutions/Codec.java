package javasolutions;

import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;

public class Codec {

  // Encode a tree to a single string
  public String serialize(TreeNode root) {
    if (root == null) {
      return null;
    }
    String serialized_string = new String();
    serialized_string = preOrderTraverse(root, serialized_string);
    serialized_string = serialized_string.substring(0, serialized_string.length() - 1);
    System.out.println(serialized_string);
    return serialized_string;
  }

  private String preOrderTraverse(TreeNode root, String output) {
    if (root != null) {
      output = String.valueOf(root.val) + ",";
      output = output + preOrderTraverse(root.left, output);
      output = output + preOrderTraverse(root.right, output);
    } else {
      output = "#,";
    }

    return output;
  }

  // Decodes your encoded data to tree.
  public TreeNode deserialize(String data) {
    if (data == null || data.isEmpty()) {
      return null;
    }
    
    Queue<String> strQueue = new LinkedList<String>(Arrays.asList(data.split(",")));
    return preOrderDeserialize(strQueue);
  }

  private TreeNode preOrderDeserialize(Queue<String> strQueue) {
    TreeNode root = null;
    String str = strQueue.poll();
    
    if (str.equals("#")) {
      return null;
    } else {
      root = new TreeNode(Integer.parseInt(str));
      root.left = preOrderDeserialize(strQueue);
      root.right = preOrderDeserialize(strQueue);
    }

    return root;
  }

  public static void main(String[] args) {
    Codec codec = new Codec();

    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    root.right.left = new TreeNode(4);
    root.right.right = new TreeNode(5);

    String str = codec.serialize(root);
    System.out.println("deserialize and serialize again");
    codec.serialize(codec.deserialize(str));
  }
}