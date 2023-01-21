// https://www.acmicpc.net/problem/2739

package main

import (
	"fmt"
)

func main() {
	var num int
	fmt.Scanln(&num)
	for i := 1; i < 10; i++ {
		fmt.Printf("%d * %d = %d\n", num, i, num * i)
	}
}