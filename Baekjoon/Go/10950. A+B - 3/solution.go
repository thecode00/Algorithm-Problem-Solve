// https://www.acmicpc.net/problem/10950

package main

import (
	"fmt"
)

func main() {
	var t int
	var a, b int
	fmt.Scan(&t)
	for i := 0; i < t; i++ {
		fmt.Scan(&a, &b)
		fmt.Println(a + b)
	}
}