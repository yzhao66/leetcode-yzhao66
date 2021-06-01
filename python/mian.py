class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        count = 0
        ret = ListNode()
        tmp = ret
        while l1 or l2 or count:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if count:
                num += count
                count -= 1
            count, num = divmod(num, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return ret.next






if __name__ == "__main__":
    l1 = ListNode()
    l1.__init__(2,4)
    l1.__init__(4,3)
    print(l1)
    l2 = ListNode()
    l2.__init__(5,6)
    l2.__init__(6,4)
    Solution.addTwoNumbers(0,l1,l2)

