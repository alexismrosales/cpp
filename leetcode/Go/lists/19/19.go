package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	szs := countNodes(head)
	// Length 1
	if n == 1 && szs == 1 {
		return nil
	}
	// If we have the same lenght we return the all the list withtout the first element
	if n == szs {
		return head.Next
	}
	traverseList(head, szs, n)
	return head
}

func countNodes(head *ListNode) int {
	n := 0
	ptr := head
	for ptr != nil {
		ptr = ptr.Next
		n++
	}
	return n
}

func traverseList(head *ListNode, szs, n int) {
	ptr := head
	var next *ListNode
	counter := 1
	for ptr != nil {
		if (szs - n) == counter {
			next = ptr.Next.Next
			ptr.Next = next
			head = ptr
			break
		} else {
			ptr = ptr.Next
		}
		counter++
	}
}
