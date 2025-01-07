# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\
        
        #Setting slow to the start of the second half of the linked list and the fast to the end of the second half of the linked list:
        slow, fast =  head, head.next
        while fast and fast.next:
            slow = slow.next #slow ends at 
            fast = fast.next.next

        #Reversing the second half of the linked list:
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        second = prev
        first = head
        #Merging the two linked lists:
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        