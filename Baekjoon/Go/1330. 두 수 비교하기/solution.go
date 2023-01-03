// https://www.acmicpc.net/problem/1330

package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	if a > b {
		println(">")
	} else if a == b {
		println("==")
	} else {
		println("<")
	}
}
