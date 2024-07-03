// src/server.ts
import { Server } from "socket.io"

const io = new Server(8080)

io.on("connection", socket => {
	console.log("A user connected")

	socket.on("chat message", msg => {
		console.log("message: " + msg)
		io.emit("chat message", msg) // Broadcast to all clients
	})

	socket.on("disconnect", () => {
		console.log("user disconnected")
	})
})
