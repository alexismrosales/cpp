package main

import (
	"math"
	"slices"
)

type MinStack struct {
	items      []int
	top        int
	minElement int
}

func Constructor() MinStack {
	return MinStack{
		items:      []int{},
		top:        -1,
		minElement: math.MaxInt,
	}
}

func (this *MinStack) Push(val int) {
	this.top++
	this.items = append(this.items, val)
	// Saving min value if there exists
	if val < this.minElement {
		this.minElement = val
	}
}

func (this *MinStack) Pop() {
	this.top--
	if this.items[this.top+1] == this.minElement {
		newStack := this.items[0:this.top]
		if len(newStack) != 0 {
			this.minElement = slices.Min(newStack)
		}
	}
}

func (this *MinStack) Top() int {
	return this.items[this.top]
}

func (this *MinStack) GetMin() int {
	return this.minElement
}
