num = int(input())

for _ in range(num):
    h, m = input().split(":")
    h = int(h)

    if h == 0:
        print(f"12:{m} AM")
    
    elif h > 0 and h < 12:
        print(f"{h:02d}:{m} AM")
    
    elif h == 12:
        print(f"{h:02d}:{m} PM")
    
    elif h > 12:
        print(f"{(h - 12):02d}:{m} PM")
