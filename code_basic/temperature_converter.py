def do_c_sang_do_f():
    while True:
        cTemp = input("xin hay nhap do c: ")
        if cTemp:
            #print(type(cTemp))
            cTemp = float(cTemp)
            fTemp = 9*cTemp/5 +32
        
            print(f"{cTemp}c is conver to {fTemp}f")
            break
        else:
            print("nhap so di ban oi")
            continue

def main():
    # print("hello word")
    do_c_sang_do_f()
if __name__ == "__main__":
    main()