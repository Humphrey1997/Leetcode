# 思路：用递归实现，很巧妙
# 收获：熟悉ListNode这一数据结构,(.val)返回值,(.next)返回下一个节点

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        l1.val += l2.val    # 将两数相加，赋值给 l1 节点
        if l1.val >= 10:
            # 这一句很巧妙的同时解决了进位和链表扩充问题
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)
            l1.val %= 10
        
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1