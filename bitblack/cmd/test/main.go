package main

import (
	"fmt"

	"sync"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/push"
)

func pushPrometheus() {
	completionTime := prometheus.NewGauge(prometheus.GaugeOpts{
		Name: "koala",
		Help: "The timestamp of the last successful completion of a DB backup.",
	})
	completionTime.SetToCurrentTime()
	completionTime.Add(1)
	if err := push.New("http://localhost:9091", "koala_db_backup").
		Collector(completionTime).
		Grouping("db", "customers").
		Grouping("instance", "koala-1").
		Push(); err != nil {
		fmt.Println("Could not push completion time to Pushgateway:", err)
	}
}

func timeTicker() {
	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()
	for i := 0; i < 10; i++ {
		fmt.Println("test")
		<-ticker.C
	}
}

func syncWaitGroup() {
	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(index int) {
			fmt.Println(index)
			wg.Done()
		}(i)

	}
	wg.Wait()
}

func main() {
	syncWaitGroup()
	fmt.Println("test")
}
