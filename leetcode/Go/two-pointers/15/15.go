package main

import "sort"

// My try
func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	triplets := [][]int{}
	// If pointer 1 is together of p2 and p3
	for p1 := 0; p1 < len(nums)-2; p1++ {
		// Avoiding duplicates
		if p1 > 0 && nums[p1] == nums[p1-1] {
			continue
		}
		p2 := p1 + 1        // Pointer next to p1 forever
		p3 := len(nums) - 1 // Last element
		for p2 < p3 {
			sum := nums[p1] + nums[p2] + nums[p3]
			if sum == 0 {
				// Adding a new triplet
				triplets = append(triplets, []int{nums[p1], nums[p2], nums[p3]})
				// Avoiding duplicates
				for p2 < p3 && nums[p2] == nums[p2+1] {
					p2++
				}
				for p2 < p3 && nums[p3] == nums[p3-1] {
					p3--
				}
				// Pointing to next elements
				p2++
				p3--
			} else if sum < 0 {
				//  Moving p2 to right if
				p2++
			} else {
				p3--
			}
		}
	}
	return triplets
}
