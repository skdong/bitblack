package main

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/coreos/etcd/clientv3"
)

func papi() {
	config := clientv3.Config{
		Endpoints:    []string{"localhost:2379"},
		DialTimeout: 50 * time.Second,
	}
	cli, err := clientv3.New(config)
	if err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
	defer cli.Close()

	ctx, cancel := context.WithTimeout(context.Background(), 120*time.Second)
	_, err = cli.Put(ctx, "/bitblack/papi", "free")
	cancel()
	if err != nil{
		fmt.Println(err)
		os.Exit(-1)
	}

	ctx, cancel = context.WithTimeout(context.Background(), 50*time.Second)
	resp, err := cli.Get(ctx, "/biitback/papi")
	cancel()

	if err != nil{
		fmt.Println(err)
		os.Exit(-1)
	}

	for _, ev := range resp.Kvs{
		fmt.Printf("%s: %s", ev.Key, ev.Value)
	}

}

func main() {
	papi()
}
