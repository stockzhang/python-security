import optparse
import socket
import threading

screenlock=threading.Semaphore(value=1)

def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send("hello world!\r\n")
        results=connSkt.recv(1024)
        screenlock.acquire()
        print("[+]%d tcp opened" % tgtPort)
        print("[+]"+str(results))
    except:
        screenlock.acquire()
        print("[-]%d tcp closed" % tgtPort)
    finally:
        screenlock.release()
        connSkt.close()

def portscan(tgtHost,tgtPorts):
    try:
        tgtIP=socket.gethostbyname(tgtHost)
    except:
        print("[-]:Cant resoved %s" % tgtHost)
        return
    try:
        tgtName=socket.gethostbyaddr(tgtIP)
        print tgtName
    except:
        print("[+]:Scan results for: %s" % tgtIP)
    socket.setdefaulttimeout(10)
    threads=[]
    for tgtPort in tgtPorts:
        print("Scaning port "+str(tgtPort))
        t=threading.Thread(target=connScan,args=(tgtHost,tgtPort))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def getpasre():
    parser=optparse.OptionParser('usage %prog -H <host> -P <port>')
    parser.add_option('-H',dest='tgtHost',type='string')
    parser.add_option('-P',dest='tgtPort',type='int')
    (options,args) = parser.parse_args()
    tgtHost=options.tgtHost
    tgtPort=options.tgtPort
    if tgtHost == None and tgtPort == None:
        print parser.usage
    else:
        print tgtHost,tgtPort

if __name__ == '__main__':
   portscan('www.dbtan.com',[80,22,443])