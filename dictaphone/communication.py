import socketio
import eventlet

class Communication:
    def __init__(self):
        self.sio = socketio.Server()
        self.app = socketio.WSGIApp(self.sio)

    def start(self, port=3000):
        @self.sio.event
        def connect(sid, environ):
            print('Client connecté:', sid)

        @self.sio.event
        def disconnect(sid):
            print('Client déconnecté:', sid)

        @self.sio.on('message')
        def handle_message(sid, data):
            print('Message reçu:', data)
            self.sio.emit('response', {'status': 'Message reçu'}, room=sid)

        print(f"Serveur de communication démarré sur le port {port}")
        eventlet.wsgi.server(eventlet.listen(('', port)), self.app)