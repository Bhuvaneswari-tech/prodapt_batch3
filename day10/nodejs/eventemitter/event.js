import EventEmitter from "events";

const emitter = new EventEmitter();

// Listener
emitter.on("greet", (name) => {
    console.log(`Hello ${name}`);
});

// Emit the event
emitter.emit("greet", "Rahul");