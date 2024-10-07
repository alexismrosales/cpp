package main

import (
	"sort"
	"strings"
)

func sortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func indexesToStrings(indexes []int, words []string) []string {
	var groupOfWords []string
	// Getting all the anagrams possible for a group
	for _, val := range indexes {
		groupOfWords = append(groupOfWords, words[val])
	}
	return groupOfWords
}

func groupAnagrams(strs []string) [][]string {
	// Anagrams would be save in groups of indexes
	indexGroupsAnagrams := make(map[string][]int)
	var groupOfAnagrams [][]string
	// Sorting every word
	for i := range strs {
		wordSorted := sortString(strs[i])
		// Saving the word in map of indexes
		indexGroupsAnagrams[wordSorted] = append(indexGroupsAnagrams[wordSorted], i)
	}
	// Getting arrays of anagrams
	for _, indexes := range indexGroupsAnagrams {
		groupOfAnagrams = append(groupOfAnagrams, indexesToStrings(indexes, strs))
	}
	return groupOfAnagrams
}
