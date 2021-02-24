"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their
nodes contains a single digit. Add thetwo numbers and return the sum as a
linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    def solution(self, list1, list2):
        answer = ListNode()
        pointer = answer
        carry = False
        while True:
            digit_sum = list1.val + list2.val
            if carry:
                digit_sum += 1
                carry = False

            if digit_sum >= 10:
                digit_sum -= 10
                carry = True

            pointer.val = digit_sum
            list1 = list1.next
            list2 = list2.next

            if list1 is None or list2 is None:
                break
            else:
                pointer.next = ListNode()
                pointer = pointer.next

        list3 = None
        if list1 is None:
            list3 = list2
        else:
            list3 = list1

        while list3 is not None:
            digit_sum = list3.val
            if carry:
                digit_sum += 1
                carry = False

            if digit_sum >= 10:
                digit_sum -= 10
                carry = True

            pointer.next = ListNode(digit_sum)
            pointer = pointer.next
            list3 = list3.next

        return answer

    def test(self):
        list1 = ListNode(2, ListNode(4, ListNode(3)))
        list2 = ListNode(5, ListNode(6, ListNode(4)))
        answer = self.solution(list1, list2)
        while answer is not None:
            print(answer.val)
            answer = answer.next


this = AddTwoNumbers()
this.test()
