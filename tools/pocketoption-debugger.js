// Made by © https://github.com/B4rCodee


const messageReceiveListeners = [receiveListener]
const messageSendListeners = [sendListener]
const decoder = new TextDecoder("utf-8");

/**
 * WebSocket Interception
 */
const sockets = []

function listen(fn = debug) {
    const originalDataGetter = Object.getOwnPropertyDescriptor(MessageEvent.prototype, "data").get;

    function dataInterceptor() {
        if (this.currentTarget instanceof WebSocket) {
            if (!sockets.includes(this.currentTarget) && !this.currentTarget.url.includes("chat")) {
                const originalSend = this.currentTarget.send;
                this.currentTarget.send = function(message) {
                    originalSend.call(this, message);
                    messageSendListeners.forEach(listener => listener(message));
                };
                sockets.push(this.currentTarget)
                this.currentTarget.addEventListener("message", (event) => {
                    
                    messageReceiveListeners.forEach(listener => listener(event.data));
                  });
            }

           // fn({ data: originalDataGetter.call(this), socket: this.currentTarget, event: this });
        }
        return originalDataGetter.call(this);
    }

    Object.defineProperty(MessageEvent.prototype, "data", {
        get: dataInterceptor,
        configurable: true
    });
}

function messageHandler(data) {
    messageReceiveListeners.forEach(listener => listener(data));
    messageSendListeners.forEach(listener => listener(data));
}

let receive = true
let send = true

const types = new Map()

let expected = ""

function receiveListener(data) {
    if (!receive || data.length < 2) return
    if (data instanceof ArrayBuffer) {
        data = decoder.decode(data)
    }

    if (data.startsWith("451-")) {
        const proc = data.replace("451-", "")
        const json = JSON.parse(proc)
        const messageType = json[0]
        expected = messageType
        return   
    }

    if (!types.has(expected && expected != "")) {
            
        types.set(expected, data)
        console.log("[RECEIVE] " + expected, ": ", data)
    }
}

function sendListener(data) {
    if (!send || data.length < 3) return

    const proc = data.replace("42", "")
    const json = JSON.parse(proc)
    const type = json[0]
    console.log("[SEND]: ", type + ": " + proc)
    if (!types.has(type)) {
            
        types.set(type, data)
        console.log(type, ": ", data)
    }
}

listen(({ data }) => messageHandler(data));