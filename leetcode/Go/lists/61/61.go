package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	// With this we avoid to make unnecesary rotations
	totalNodes := countNodes(head)
	// If we got no elements
	if totalNodes == 0 {
		return nil
	}
	// If there no rest we know the list still the same
	if k%totalNodes == 0 {
		return head
	}
	timesToRotate := k % totalNodes
	return rotatingNtimes(head, timesToRotate)
}

// Counting Nodes
func countNodes(head *ListNode) int {
	if head == nil {
		return 0
	}
	ptr := head
	n := 0
	for ptr != nil {
		n++
		ptr = ptr.Next
	}
	return n
}

// rotatingNtimes
func rotatingNtimes(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	for range k {
		ptr := head
		// Traversing until the last element
		for ptr.Next.Next != nil {
			ptr = ptr.Next
		}
		end := ptr.Next
		ptr.Next = nil
		end.Next = head
		head = end
	}
	return head
}
