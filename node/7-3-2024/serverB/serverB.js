"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// import { WebSocketServer } from "ws"
var ws_1 = require("ws");
var wss = new ws_1.WebSocketServer({ port: 8080 });
wss.on("connection", function (ws) {
    console.log("New client connected!");
    ws.on("message", function (message) {
        console.log("Received message: ".concat(message));
        // Broadcast the message to all connected clients
        wss.clients.forEach(function (client) {
            if (client.readyState === ws_1.WebSocket.OPEN) {
                client.send(message.toString());
            }
        });
    });
    ws.on("close", function () {
        console.log("Client disconnected");
    });
});
console.log("WebSocket server started on ws://localhost:8080");
