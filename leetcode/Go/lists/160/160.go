package main

import (
	"fmt"
)

// Basic idea: Traverse both lists and save their directions in an array and compare
// them beggining from the end
type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	arrA := traverseList(headA)
	arrB := traverseList(headB)
	return compareData(arrA, arrB)
}

// Getting data into an array
func traverseList(head *ListNode) []*ListNode {
	ptr := head
	var nodes []*ListNode
	for ptr != nil {
		nodes = append(nodes, ptr)
		fmt.Println(nodes)
		ptr = ptr.Next
	}

	return nodes
}

// Comparing both arrays from the end
func compareData(arrA, arrB []*ListNode) *ListNode {
	sizeA := len(arrA)
	sizeB := len(arrB)
	it := min(sizeA, sizeB)

	for range it {
		if arrA[sizeA-1] != arrB[sizeB-1] {
			// If the last element is different
			if sizeA == len(arrA) {
				return nil
			}
			return arrA[sizeA]
		}
		sizeA--
		sizeB--
	}

	// If one linked list has only one element we reach this state
	return arrA[sizeA]
}
