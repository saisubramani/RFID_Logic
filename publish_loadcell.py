import time
import zmq

class read_from_file():
    def __init__(self):
        self.file=open('Log_Load_cell.log','r')
        self.loadcell_port = "5555"
        self.RFID_port = "6666"
        self.EPC = '01.12000A.4570000.45F56872/01.13000A.4580000.45F56872/01.14000A.4590000.45F56872/01.15000A.4600000.45F56872/01.16000A.4610000.45F56872'

        ''' RFID SUBCRIPTION'''
        self.context_RFID_SUB = zmq.Context()
        self.socket_RFID_SUB = self.context_RFID_SUB.socket(zmq.SUB)
        self.socket_RFID_SUB.connect('tcp://127.0.0.1:'+str(self.RFID_port))
        self.socket_RFID_SUB.subscribe("")
        print("Subscribed to RFID data ...")
        ''' RFID SUBCRIPTION'''

        '''RFID PUBLISHING'''
        self.context_RFID_PUB = zmq.Context()
        self.socket_RFID_PUB = self.context_RFID.socket(zmq.PUB)
        self.socket_RFID_PUB.bind('tcp://127.0.0.1:'+str(self.RFId_port))
        '''RFID PUBLISHING'''

        self.lines = self.file.readlines()
        self.count = 0
        self.Flag = True
        self.logs = {}
        for line in self.lines:
            self.logs[self.count] = line.strip()
            self.count += 1
        self.list1=[]
        self.list2=[]
        for i in range(len(self.logs)):
            values=self.logs[i]
            values1=values.split('     ')
            self.list1.append(values1[0])
            self.list2.append(values1[1])
        self.limit = len(self.list1)
        print("Limit:",self.limit)       


    def Load_cell(self,ct):
        if ct!=0:
            sleep=float(self.list2[ct])/1000
            time.sleep(sleep)
        return self.list1[ct]

    def publish_to_loadcell(self):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        ct = 0
        socket.bind('tcp://127.0.0.1:'+str(self.loadcell_port))
        while self.Flag:
            if ct > self.limit-1:
                break
            else:           
                data = self.Load_cell(ct)
                print("data:",data)
                socket.send_pyobj({'data':data})
                RFID_trigger = self.socket_RFID_SUB.recv_pyobj()
                trigger = int(msg.get('trigger'))
                if trigger == 1:
                    self.socket_RFID.send_pyobj(self.EPC)

                ct+=1

    
    
    
a = read_from_file()
a.publish_to_loadcell()
