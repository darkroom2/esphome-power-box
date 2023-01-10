import serial


def main():
    ser = serial.Serial("/dev/ttyUSB0")
    print(ser.name)
    ser.write(b"Hello World")
    ser.close()


if __name__ == "__main__":
    main()
