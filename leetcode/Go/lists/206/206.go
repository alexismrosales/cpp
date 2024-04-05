package main

// Using multiple temporal variables and change their pointer direction
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var ptr, prev, next *ListNode = head, nil, nil
	// Changing pointer with tmp vars
	for ptr != nil {
		next = ptr.Next
		ptr.Next = prev
		prev = ptr
		ptr = next
	}
	return prev
}
