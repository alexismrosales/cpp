package main

import "sort"

func twoSum(nums []int, target int) []int {
	indexes := make(map[int][]int)
	for i, num := range nums {
		indexes[num] = append(indexes[num], i)
	}
	sortedNums := make([]int, len(nums))
	copy(sortedNums, nums)
	sort.Ints(sortedNums)

	p1, p2 := 0, len(nums)-1
	for p1 < p2 {
		sum := sortedNums[p1] + sortedNums[p2]
		if sum == target {
			break
		} else if sum < target {
			p1++
		} else {
			p2--
		}
	}
	index1 := indexes[sortedNums[p1]][0]
	// Deleting used index
	indexes[sortedNums[p1]] = indexes[sortedNums[p1]][1:]
	index2 := indexes[sortedNums[p2]][0]
	return []int{index1, index2}
}
