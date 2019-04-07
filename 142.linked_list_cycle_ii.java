// ### [142\. Linked List Cycle IICopy for MarkdownCopy for Markdown](https://leetcode.com/problems/linked-list-cycle-ii/)

// Difficulty: **Medium**


// Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

// To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

// **Note:** Do not modify the linked list.

// **Example 1:**

// ```
// Input: head = [3,2,0,-4], pos = 1
// Output: tail connects to node index 1
// Explanation: There is a cycle in the linked list, where tail connects to the second node.
// ```

// ![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

// **Example 2:**

// ```
// Input: head = [1,2], pos = 0
// Output: tail connects to node index 0
// Explanation: There is a cycle in the linked list, where tail connects to the first node.
// ```

// ![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

// **Example 3:**

// ```
// Input: head = [1], pos = -1
// Output: no cycle
// Explanation: There is no cycle in the linked list.
// ```

// ![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

// **Follow up**:  
// Can you solve it without using extra space?


// #### Solution

// Language: **Java**

// ```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

// http://www.cnblogs.com/wuyuegb2312/p/3183214.html
// 从0时刻开始，
// p1运动了(L+x)距离，扣除进入环之前的L，剩余x，对应圆环上的位置（可以看作圆环上的刻度，以入口为0刻度开始）是x%R
// p2速度是p1的2倍，那么一共运动了2*(L+x)距离，扣除进入环之前的L，剩余[2*(L+x) - L]，那么对应圆环上的位置(刻度)为[2*(L+x)-L]%R
// 用刻度的视角，类比钟表表盘 这样好理解些吧
public class Solution {
  public ListNode detectCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while(true) {
      if(fast == null || fast.next == null) {
        return null;
    }
     
     slow = slow.next;
     fast = fast.next.next;
     
     if(slow == fast) {
      break;
      }
    }

    slow = head;
    while(slow != fast) {
      slow = slow.next;
      fast = fast.next;
    }
    
    return slow;
   }
}
