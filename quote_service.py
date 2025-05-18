import zmq
import random

quotes = [
    "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
    "Courage is resistance to fear, mastery of fear - not absence of fear. - Mark Twain",
    "Only put off until tomorrow what you are willing to die having left undone. - Pablo Picasso",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Act as if what you do makes a difference. It does. - William James",
    "The best way to predict the future is to create it. - Peter Drucker",
    "The best revenge is massive success. - Frank Sinatra",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Don't stop when you're tired. Stop when you're done. - Wesley Snipes",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "I hated every minute of training, but I said 'Don't Quit. Suffer now and live the rest of your life as a champion.' - Muhammad Ali"
]

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    
    print("Quote service starting on port 8765...")
    socket.bind("tcp://*:8765")
    
    try:
        while True:
            # wait for request
            message = socket.recv_string()
            print(f"Received request: {message}")
            
            # determine response
            if message.lower() in ["quote", "get quote", "motivate"]:
                quote = random.choice(quotes)
            else:
                quote = "ERROR: Invalid request. Try 'quote' or 'motivate'."

            # send response
            print(f"Sending quote: {quote}")
            socket.send_string(quote)

    except KeyboardInterrupt:
        print("\nQuote service shutting down...")
    finally:
        socket.close()
        context.term()

if __name__ == "__main__":
    main()
