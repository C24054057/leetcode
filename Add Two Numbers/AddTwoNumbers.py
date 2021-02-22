# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self, item):
        # item may be a val or a node
        # we need to may sure item is a node
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        
class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = SingleLinkedList()
        ptr_1 = l1
        ptr_2 = l2
        cout = 0
        while ptr_1 or ptr_2:
            cin = cout
            cout = 0
            if not ptr_1:
                Sum = ptr_2.val + cin
                ptr_2 = ptr_2.next
            elif not ptr_2:
                Sum = ptr_1.val + cin
                ptr_1 = ptr_1.next
            else:
                Sum = ptr_1.val + ptr_2.val + cin
                ptr_1 = ptr_1.next
                ptr_2 = ptr_2.next
            if Sum >= 10:
                cout = 1
            output.addNode(Sum % 10)

        if cout == 1:
            output.addNode(cout)

        # ptr = output.head
        # while ptr:            
        #     print(ptr.val, end = ' ')
        #     ptr = ptr.next

        return output.head



# l1 = SingleLinkedList()
# for _ in range(20):
#     l1.addNode(1)
# l2 = SingleLinkedList()
# for _ in range(10):
#     l2.addNode(2)

# s = Solution()
# s.addTwoNumbers(l1.head, l2.head)