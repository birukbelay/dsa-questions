package main

import "fmt"

func main() {
	var pairs = make(map[int]int)
	commits := map[int]int{
		1: 1,
		3: 0,
		4: 0,
		5: 0,
	}
	// x := [5]int{10, 20, 30, 40, 50}
	b, ok := commits[0]
	a := pairs[1]
	fmt.Println(a, pairs, "b-", b, ok)
}

func numIdenticalPairs(nums []int) int {
	var count = 0
	var pairs = make(map[int]int)
	for _, num1 := range nums {
		a := pairs[num1]

		count += a
		a++
		pairs[num1] = a
	}
	return count
}
