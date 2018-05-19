package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
)

// recursive function to square all items in an array and add them
// together (excluding negatives)
func square(num, curr, size int, list []int) int {
    // base case
    if curr == size {
        return 0
    }

    idx := curr
    curr += 1
    // avoid index out of bounds
    if curr != size {
        idx += 1
    }
    // ignore negatives
    if num < 0 {
        num = 0
    }
    return square(list[idx] , curr, size, list) + (num * num)
}

// reads in stdin and outputs summation of squares to stdout
func main() {
    in := bufio.NewScanner(os.Stdin)
    in.Scan()
    numInputs, err := strconv.Atoi(in.Text())
    in.Scan()
    if err != nil {
        fmt.Println("error")
    }
    for i := 0; i < numInputs; i++ {
        numList, err := strconv.Atoi(in.Text())
        in.Scan()
        if err != nil {
            fmt.Println("error")
        }
        numbers := strings.Split(in.Text(), " ")
        list := make([]int, numList)
        for j := 0; j < numList; j++ {
             list[j], err = strconv.Atoi(numbers[j])
             if err != nil {
                 fmt.Println("error")
             }
        }
        fmt.Println(square(list[0], 0, numList, list))
        if ((i + 1) != numInputs) {
            in.Scan()
        }
    }
}
