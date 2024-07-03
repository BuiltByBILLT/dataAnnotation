"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// src/server.ts
const socket_io_1 = require("socket.io");
const io = new socket_io_1.Server(3000);
io.on("connection", socket => {
    console.log("A user connected");
    socket.on("chat message", msg => {
        console.log("message: " + msg);
        io.emit("chat message", msg); // Broadcast to all clients
    });
    socket.on("disconnect", () => {
        console.log("user disconnected");
    });
});
