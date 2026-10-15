# Client-Server Communication System

A Python TCP client-server application developed as a university group project at Wilfrid Laurier University.

## Overview

This project demonstrates communication between multiple clients and a central server using TCP sockets. The server supports up to three simultaneous client connections and uses multithreading to handle client requests.

## Features

- **Client Connections:** Connect multiple clients to a central server.
- **Multithreading:** Handle client connections using separate threads.
- **File Listing:** Allow clients to request a list of available files.
- **Connection Status:** Check connection status using JSON messages.
- **Disconnect Command:** Allow clients to disconnect from the server.
- **Thread Safety:** Use thread locks to help manage shared resources.

## Technologies Used

- Python
- TCP Sockets
- Multithreading
- JSON

## How to Run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Start the server using `python server.py`.
5. Open another terminal and start a client using `python client.py`.

## Project Type

University Group Project — Wilfrid Laurier University
