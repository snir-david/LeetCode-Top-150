# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        curr_node = head
        node_list = []
        for i in range(1, right + 1):
            if left <= i <= right:
                node_list.append(curr_node)
            curr_node = curr_node.next
        j = 0
        k = len(node_list)-1
        while k > j :
            tmp_val = node_list[j].val
            node_list[j].val = node_list[k].val
            node_list[k].val = tmp_val
            j += 1
            k -=1
        return head


if __name__ == '__main__':
    s = Solution()
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = ListNode(5)

    h = s.reverseBetween(head, 1, 1)
    print(5)
