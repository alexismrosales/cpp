package main

import "sort"

type mapKV struct {
	Key   int
	Value int
}

func topKFrequent(nums []int, k int) []int {
	freqs := make(map[int]int)
	topFreqs := make([]int, k)
	for _, num := range nums {
		freqs[num]++
	}

	var kv []mapKV
	// Getting map in struct
	for k, v := range freqs {
		kv = append(kv, mapKV{Key: k, Value: v})
	}
	sort.Slice(kv, func(i, j int) bool {
		return kv[i].Value > kv[j].Value
	})
	for i := 0; i < k; i++ {
		topFreqs[i] = kv[i].Key
	}
	return topFreqs
}
