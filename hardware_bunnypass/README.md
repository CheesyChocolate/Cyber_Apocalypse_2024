# BunnyPass

As you discovered in the PDF, the production factory of the game is revealed.
This factory manufactures all the hardware devices and custom silicon chips (of
common components) that The Fray uses to create sensors, drones, and various
other items for the games. Upon arriving at the factory, you scan the networks
and come across a RabbitMQ instance. It appears that default credentials will
work.

## How to Play

The challenge provides a URL to a RabbitMQ instance. as said in the description,
the default credentials will work.

```
username: admin
password: admin
```

so from here on, we just need to look around the RabbitMQ instance to find the
flag.

> Queue => factory_idle => Get messages

In the field Message we enter 7 and click on "Get Message(s)".

The flag is in the last message body.


## Flag

```
HTB{th3_hunt3d_b3c0m3s_th3_hunt3r}
```
