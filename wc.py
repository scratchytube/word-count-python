import sys
import argparse


def count(data: bytes) -> int:
    return len(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "-bytes", action="store_true", help="Count bytes")
    flags = parser.parse_args()
    
    data = sys.stdin.buffer.read()
    
    if flags.bytes:
        print(count(data))
        
if __name__ == "__main__":
    main()
