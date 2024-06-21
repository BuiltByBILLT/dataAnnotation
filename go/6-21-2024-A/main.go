package main

import (
    "fmt"
    "sync"
    "time"
)

func processItem(item int, wg *sync.WaitGroup) {
    defer wg.Done()

    // Simulating some time-consuming task
    time.Sleep(time.Second)
    fmt.Println("Processed item:", item)
}

func main() {
    items := []int{1, 2, 3, 4, 5}

    var wg sync.WaitGroup

    for _, item := range items {
        wg.Add(1)
        go processItem(item, &wg) // Spawning a new goroutine for each item
    }

    wg.Wait() // Waiting for all goroutines to finish
    fmt.Println("All items processed.")
}