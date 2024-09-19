import ydlidar_x2
import socket
import time

def main():
    port =  '/dev/ttyUSB0'
    lid = ydlidar_x2.YDLidarX2(port)
    lid.connect()
    lid.start_scan()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    UDP_IP, UDP_PORT = "192.168.1.27",2222

    angles = list(range(0, 360))

    try:
        while True:
            if lid.available:
                distances = list(lid.get_data())
                angleDistancePair = list(map(list, zip(angles, distances)))
                MESSAGE = str(list(angleDistancePair))
                # print(MESSAGE)
                sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT)) # 2222 - port on client IP
                
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    lid.stop_scan()
    lid.disconnect()
    return 

if __name__ == "__main__":
    main()
    print("Done")