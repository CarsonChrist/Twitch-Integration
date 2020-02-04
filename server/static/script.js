var socket = io();

socket.on('connect', function() {
    console.log("connected");
});

socket.on('left', function() {
    console.log("left");
});

socket.on('right', function() {
    console.log("right");
});