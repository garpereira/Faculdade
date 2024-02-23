# Java Socket Chat

This is a sample project that demonstrates the creation of a simple Java chat application using socket communication. The project is divided into server and client components, allowing users to communicate in real-time.

## Table of Contents

- [Authors](#authors)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Notes](#notes)
- [License](#license)

## Authors

- [Matheus Silva](https://github.com/matheuxito) | [LinkedIn](https://www.linkedin.com/in/matheuxito/)
- [Gabriel Pereira](https://github.com/garpereira) | [LinkedIn](https://www.linkedin.com/in/garpereira/)

## Features

- Clients and server communicate via TCP/IP sockets.
- Clients can connect to the server and exchange messages.
- Each message includes sender information, content, and timestamp.

## Project Structure

```
src
├── server
│   └── ServerMain.java
└── client
    └── ClientMain.java

```

## Getting Started

1. Compile the server and client classes.
   ```shell
   javac server/*.java
   javac client/*.java
   ```

2. Start the server.
   ```shell
   java server.ServerMain
   ```

3. Start one or more clients.
   ```shell
   java client.ClientMain
   ```

## Notes

- Make sure the server is running before starting clients.
- Exchanged messages are displayed in the console.
- This is a sample project and can be extended with additional features and enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
