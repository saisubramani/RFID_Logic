import zmq

class connection():
    def __init__(self):
        self.loadcell_port = "5555"
        self.RFId_port = "6666" 

        '''RFID PUBLISHING'''
        self.context_RFID = zmq.Context()
        self.socket_RFID = self.context_RFID.socket(zmq.PUB)
        self.socket_RFID.bind('tcp://127.0.0.1:'+str(self.RFId_port))
        '''RFID PUBLISHING'''

        ''' LOADCELL SUBCRIPTION'''
        self.context_loadcell = zmq.Context()
        self.socket_loadcell = self.context_loadcell.socket(zmq.SUB)
        self.socket_loadcell.connect('tcp://127.0.0.1:'+str(self.loadcell_port))
        self.socket_loadcell.subscribe("")
        ''' LOADCELL SUBCRIPTION'''

        

        print("Subscribed to loadcell data ...")
        self.total = 0
        self.process()

    def process(self):
        while True:
            msg = self.socket_loadcell.recv_pyobj()
            data = float(msg.get('data'))
            print("Received data:",data)
            self.total = self.total+data
            if self.total>0.150:
                self.prev_total = self.total
                self.socket_RFID.send_pyobj({'trigger':1})
                self.total = 0





        self.socket_loadcell.close()
        self.context_loadcell()
    

a = connection()