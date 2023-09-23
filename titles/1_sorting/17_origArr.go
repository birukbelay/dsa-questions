package main

import (
	"log"
	"sort"
)
func findOriginalArray(changed []int) {
    a := sort.IntSlice(changed[0:])
	sort.Sort(a)
	log.Println(a)
	// m := make(map[int]int)
	// arr:=[]int{}

	for i, v := range a {
		pos := sort.SearchInts(a, v*2)
		_, ok:=m[i*2];
		_, ok2:=m[i]
		if !ok && !ok2{
			m[i]=1
			m[pos]=1
			arr=append(arr, v)
		}
		

	// }
	


}

func main(){
	// maps:=[2, 4,5,1]
	b := [...]int{2, 4,5,1}
	findOriginalArray(b)
}