# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        digit = 0

        dummy = ListNode(0)
        result_current = dummy

        current = l1
        current2 = l2

        while current is not None or current2 is not None or carry > 0:
            val1 = current.val if current is not None else 0
            val2 = current2.val if current2 is not None else 0

            somme: int = val1 + val2 + carry
            digit: int = somme % 10
            carry: int = somme // 10

            result_current.next = ListNode(digit)
            result_current = result_current.next

            if current is not None:
                current = current.next
            if current2 is not None:
                current2 = current2.next

        if current:
            print(f"Current : {current.val}")

        return dummy.next


def create_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print("[" + ", ".join(values) + "]")


p = Solution()
l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])

result = p.addTwoNumbers(l1, l2)
print_linked_list(result)
