// https://www.acmicpc.net/problem/15552

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	var n int
	fmt.Scanln(&n)

	var a, b int
	for i := 0; i < n; i++ {

		fmt.Fscanln(reader, &a, &b)
		fmt.Fprintln(writer, a + b)
	}
	writer.Flush()	// 빠른 입출력 사용시 반드시 Flush()를 사용해야 함
}

