// src/services/communicationService.js
import { io } from 'socket.io-client';

class CommunicationService {
  constructor() {
    this.socket = null;
  }

  connect(ipAddress) {
    this.socket = io(`http://${ipAddress}:3000`);
    
    this.socket.on('connect', () => {
      console.log('Connected to Raspberry Pi');
    });

    this.socket.on('disconnect', () => {
      console.log('Disconnected from Raspberry Pi');
    });
  }

  sendData(data) {
    if (this.socket) {
      this.socket.emit('data', data);
    }
  }

  onReceiveData(callback) {
    if (this.socket) {
      this.socket.on('data', callback);
    }
  }
}

export default new CommunicationService();