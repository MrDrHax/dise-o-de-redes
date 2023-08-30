from bitarray import bitarray

def ipToBits(ip : str):
    ip = ip.split('.')
    return '{0:08b}{1:08b}{2:08b}{3:08b}'.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))

def getRequiredBits(hosts):
    hosts += 1
    return len("{0:b}".format(hosts))

def bitsToIP(bits):
    return f"{int(bits[0:8], 2)}.{int(bits[8:16], 2)}.{int(bits[16:24], 2)}.{int(bits[24:], 2)}"

class calc:
    ip : str
    mask : str
    originalMask : str
    ip_range : str
    ip_max : str

    requiredBits : int
    blockedBits : int

    submasks = []

    def __init__(self, ip, computers :int, originalMask: int) -> None:
        self.requiredBits = getRequiredBits(computers)
        self.blockedBits = 32 - self.requiredBits
        a = ["1" for i in range(self.blockedBits)]
        a += ["0" for i in range(self.requiredBits)]
        self.mask = ''.join(a)
        self.originalMask = originalMask

        submasks = []
        leftBits = self.blockedBits - originalMask

        for i in range(2 ** leftBits):
            submasks.append("{0:032b}".format(i))
            submasks[-1] = submasks[-1][-leftBits:]
        
        if not submasks:
            build = ''
        else:
            build = submasks.pop(0)

        self.ip = ip[:originalMask] + build + ''.join(["0" for i in range(self.requiredBits)])
        self.ip_max = ip[:originalMask] + build + ''.join(["1" for i in range(self.requiredBits)])

        ip1 = bitsToIP(self.ip[:31] + "1")
        ip2 = bitsToIP(self.ip_max[:31] + "0")

        self.ip_range = f"{ip1} - {ip2}"

        self.submasks = submasks

def calculate(processes : list, ip, mask):
    ip = ipToBits(ip)
    
    nodes = [calc(ip, processes.pop(0), mask)]

    for process in processes:
        pass

calculate([
    115,80,
], '140.35.0.0', 17)

print(bitsToIP('10001100001000110000000000000000'))