// src/server.ts
import * as WebSocket from "ws"

const wss = new WebSocket.Server({ port: 8080 })

wss.on("connection", (ws: WebSocket) => {
	console.log("Client connected")

	ws.on("message", (message: string) => {
		console.log(`Received message => ${message}`)

		// Broadcast the message to all connected clients
		wss.clients.forEach(client => {
			if (client !== ws && client.readyState === WebSocket.OPEN) {
				client.send(message)
			}
		})
	})

	ws.on("close", () => {
		console.log("Client disconnected")
	})
})

console.log("WebSocket server started on port 8080")
