// import { WebSocketServer } from "ws"
import { WebSocketServer, WebSocket } from "ws"

const wss = new WebSocketServer({ port: 8080 })

wss.on("connection", ws => {
	console.log("New client connected!")

	ws.on("message", message => {
		console.log(`Received message: ${message}`)

		// Broadcast the message to all connected clients
		wss.clients.forEach(client => {
			if (client.readyState === WebSocket.OPEN) {
				client.send(message.toString())
			}
		})
	})

	ws.on("close", () => {
		console.log("Client disconnected")
	})
})

console.log("WebSocket server started on ws://localhost:8080")
