package javasolutions.p297;

import javasolutions.TreeNode;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Arrays;

public class CodecRecursive {
  private static final String NULL_NODE = "#";
  private static final String SPLITER = ",";

  public String serialize(TreeNode root) {
    if(root == null) return null;

    StringBuilder answer = new StringBuilder();
    serializeHelper(root, answer);

    return answer.toString();
  }

  private void serializeHelper(TreeNode node, StringBuilder answer) {
    if(node == null) {
      answer.append(NULL_NODE).append(SPLITER);
    } else {
      answer.append(String.valueOf(node.val)).append(SPLITER);
      serializeHelper(node.left, answer);
      serializeHelper(node.right, answer);
    }
  }

  public TreeNode deserialize(String data) {
    if(data == null || data.isEmpty()) return null;
    
    Queue<String> queue = new LinkedList<>();
    queue.addAll(Arrays.asList(data.split(",")));

    return deserializeHelper(queue);
  }

  private TreeNode deserializeHelper(Queue<String> data) {
    String valueStr = data.poll();

    if(valueStr.equals(NULL_NODE)) {
      return null;
    } else {
      TreeNode node = new TreeNode(Integer.parseInt(valueStr));
      node.left = deserializeHelper(data);
      node.right = deserializeHelper(data);
      
      return node;
    }
  }

  public static void main(String[] args) {
    CodecRecursive cal = new CodecRecursive();

    TreeNode test = TreeNode.dummyTree();
    String answer1 = cal.serialize(test);
    System.out.println(answer1);
    System.out.println(cal.serialize(cal.deserialize(answer1)));
  }
}