package main

import (
	"fmt"
	"time"

	//"github.com/coreos/etcd/clientv3"
	"github.com/go-redis/redis"
)

/*
func papi() {
	config := clientv3.Config{
		Endpoints:   []string{"localhost:2379"},
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
	if err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}

	ctx, cancel = context.WithTimeout(context.Background(), 50*time.Second)
	resp, err := cli.Get(ctx, "/biitback/papi")
	cancel()

	if err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}

	for _, ev := range resp.Kvs {
		fmt.Printf("%s: %s", ev.Key, ev.Value)
	}

}
*/

func ExampleNewClient() {
	client := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password set
		DB:       0,  // use default DB
	})
	defer client.Close()

	pong, err := client.Ping().Result()
	fmt.Println(pong, err)
	// Output: PONG <nil>
	err = client.Set("koala", "hello", 0).Err()
	if err != nil {
		panic(err)
	}
	val, err := client.Get("koala").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(val)
	err = client.SetNX("nx_koala", "hello", 10*time.Second).Err()
	if err != nil {
		panic(err)
	}
	//time.Sleep(11 * time.Second)
	val, err = client.Get("nx_koala").Result()
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	fmt.Println(val)

	pubsub := client.Subscribe("koala")
	_, err = pubsub.Receive()
	if err != nil {
		panic(err)
	}
	ch := pubsub.Channel()
	err = client.Publish("koala", "hello").Err()
	if err != nil {
		panic(err)
	}
	time.AfterFunc(time.Second*10, func() {
		_ = pubsub.Close()
	})
	for msg := range ch {

		fmt.Println(msg.Channel, msg.Payload)
	}
}

func main() {
	ExampleNewClient()
}
