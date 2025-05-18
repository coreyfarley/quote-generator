import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    
    # connect to the quote service
    print("Connecting to quote service...")
    socket.connect("tcp://localhost:8765")
    
    try:
        print("Requesting a quote...")
        socket.send_string("Get Quote")
            
        # get the reply
        quote = socket.recv_string()
        print(f"Received quote: {quote}")
            
    except KeyboardInterrupt:
        print("Client interrupted. Shutting down...")
        
    finally:
        socket.close()
        context.term()

if __name__ == "__main__":
    main()
