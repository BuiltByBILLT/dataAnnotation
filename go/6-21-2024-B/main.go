package main

import (
	"fmt"
	"sync"
	"time"
)

// processItem simulates a time-consuming task
func processItem(item int, wg *sync.WaitGroup, results chan<- string) {
    defer wg.Done()
    
    // Simulate time-consuming processing
    time.Sleep(time.Second)
    result := fmt.Sprintf("Processed item: %d", item)
    results <- result // Send result to the channel
}

func main() {
    items := []int{1, 2, 3, 4, 5}
    results := make(chan string, len(items)) // Buffered channel

    var wg sync.WaitGroup

    // Spawn a goroutine for each item to process it concurrently
    for _, item := range items {
        wg.Add(1)
        go processItem(item, &wg, results)
    }

    // Close the results channel once all items are processed
    go func() {
        wg.Wait()
        close(results)
    }()

    // Collect and print results
    for result := range results {
        fmt.Println(result)
    }

    fmt.Println("All items processed.")
}