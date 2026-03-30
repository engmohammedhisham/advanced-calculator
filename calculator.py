import math
import matplotlib.pyplot as plt

# ==========================
# functions
# ==========================
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Division by zero"
    return a/b
def power(a,b):
    return a**b
def sqrt(a):
    return a**0.5
def trig(func,angle):
    rad=math.radians(angle)
    if func=='sin':
        return round(math.sin(rad),5)
    if func=='cos':
        return round(math.cos(rad),5)
    if func=='tan':
        return round(math.tan(rad),5)
    if func=='cot':
        return round(1/math.tan(rad),5)
    if func=='sec':
        return round(1/math.cos(rad),5)
    if func=='csc':
        return round(1/math.sin(rad),5)
def convert_number(value,conv_type):
    if conv_type=='Dec2Bin':
        return bin(int(value))[2:]
    if conv_type=='Bin2Dec':
        return int(value,2)
    if conv_type=='Dec2Oct':
        return oct(int(value))[2:]
    if conv_type=='Oct2Dec':
        return int(value,8)
    if conv_type=='Dec2Hex':
        return hex(int(value))[2:]
    if conv_type=='Hex2Dec':
        return int(value,16)
def convert_units(value,conv_type):
    if conv_type=='m2cm':
        return value*100
    if conv_type=='cm2m':
        return value/100
    if conv_type=='km2m':
        return value*1000
    if conv_type=='m2km':
        return value/1000
    if conv_type=='mile2km':
        return value*1.60934
    if conv_type=='km2mile':
        return value/1.60934
    if conv_type=='kg2g':
        return value*1000
    if conv_type=='g2kg':
        return value/1000
    if conv_type=='lb2kg':
        return value*0.453592
    if conv_type=='kg2lb':
        return value/0.453592
    if conv_type=='l2ml':
        return value*1000
    if conv_type=='ml2l':
        return value/1000
def percentage(value,total):
    return (value/total)*100
# ==========================
# curruncies
# ==========================
currency_rates={
    'USD':1,'EUR':0.91,'EGP':30.9,'JPY':150.5,'GBP':0.8,
    'AUD':1.5,'CAD':1.3,'CHF':0.92,'INR':83.5,'CNY':7.2
}
# ==========================
# main menu
while True:
    print("\n=== Main Menu ===")
    print("1. Calculator")
    print("2. Areas & Volumes")
    print("3. Currency Conversion")
    print("4. Unit Conversion")
    print("5. Graph")
    print("6. Play XO")
    print("7. Exit")
    choice=input("Choose an option (1-7): ").strip()
# ================== Calculator ==================
    if choice=='1':
        while True:
            print("\n--- Calculator ---")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Power (^)")
            print("6. Square root (√)")
            print("7. Trigonometric functions")
            print("8. Number conversion (Decimal/Binary/Octal/Hex)")
            print("9. Unit conversion")
            print("10. Percentage (%)")
            print("0. Back to Main Menu")
            op=input("Choose operation (0-10): ").strip()
            if op=='0':
                break
            if op=='1':
                a=float(input("Enter first number: "))
                b=float(input("Enter second number: "))
                result=add(a,b)
                print("Result:",result)
            if op=='2':
                a=float(input("Enter first number: "))
                b=float(input("Enter second number: "))
                result=subtract(a,b)
                print("Result:",result)
            if op=='3':
                a=float(input("Enter first number: "))
                b=float(input("Enter second number: "))
                result=multiply(a,b)
                print("Result:",result)
            if op=='4':
                a=float(input("Enter first number: "))
                b=float(input("Enter second number: "))
                result=divide(a,b)
                print("Result:",result)
            if op=='5':
                a=float(input("Enter base number: "))
                b=float(input("Enter exponent: "))
                result=power(a,b)
                print("Result:",result)
            if op=='6':
                a=float(input("Enter number for square root: "))
                result=sqrt(a)
                print("Result:",result)
            if op=='7':
                angle=float(input("Enter angle in degrees: "))
                result_sin=trig('sin',angle)
                print("Sin:",result_sin)
                result_cos=trig('cos',angle)
                print("Cos:",result_cos)
                result_tan=trig('tan',angle)
                print("Tan:",result_tan)
                result_cot=trig('cot',angle)
                print("Cot:",result_cot)
                result_sec=trig('sec',angle)
                print("Sec:",result_sec)
                result_csc=trig('csc',angle)
                print("Csc:",result_csc)
            if op=='8':
                num=input("Enter number for conversion: ")
                conv_type=input("Choose conversion (Dec2Bin/Bin2Dec/Dec2Oct/Oct2Dec/Dec2Hex/Hex2Dec): ")
                result=convert_number(num,conv_type)
                print("Result:",result)
            if op=='9':
                val=float(input("Enter value for unit conversion: "))
                unit_type=input("Choose unit conversion: ")
                result=convert_units(val,unit_type)
                print("Result:",result)
            if op=='10':
                val=float(input("Enter value: "))
                total=float(input("Enter total: "))
                result=percentage(val,total)
                print("Percentage:",result,"%")
# ================== Areas & Volumes ==================
    if choice=='2':
        print("\n--- Areas & Volumes ---")
        print("Shapes: Square, Rectangle, Circle, Triangle\n Cube, RectangularPrism, Sphere, Cylinder, Cone")
        shape=input("Choose shape: ").strip().lower()
        if shape=='square':
            side=float(input("Enter side length: "))
            area=side**2
            print("Area:",area)
        if shape=='rectangle':
            width=float(input("Enter width: "))
            height=float(input("Enter height: "))
            area=width*height
            print("Area:",area)
        if shape=='circle':
            radius=float(input("Enter radius: "))
            area=round(math.pi*radius**2,2)
            print("Area:",area)
        if shape=='triangle':
            base=float(input("Enter base: "))
            height=float(input("Enter height: "))
            area=0.5*base*height
            print("Area:",area)
        if shape=='cube':
            side=float(input("Enter side length: "))
            volume=side**3
            print("Volume:",volume)
        if shape=='rectangularprism':
            l=float(input("Enter length: "))
            w=float(input("Enter width: "))
            h=float(input("Enter height: "))
            volume=l*w*h
            print("Volume:",volume)
        if shape=='sphere':
            r=float(input("Enter radius: "))
            volume=round(4/3*math.pi*r**3,2)
            print("Volume:",volume)
        if shape=='cylinder':
            r=float(input("Enter radius: "))
            h=float(input("Enter height: "))
            volume=round(math.pi*r**2*h,2)
            print("Volume:",volume)
        if shape=='cone':
            r=float(input("Enter radius: "))
            h=float(input("Enter height: "))
            volume=round(1/3*math.pi*r**2*h,2)
            print("Volume:",volume)
# ================== Currency Conversion ==================
    if choice=='3':
        print("\n--- Currency Conversion ---")
        print("Available currencies:",', '.join(currency_rates.keys()))
        amount=float(input("Enter amount: "))
        from_cur=input("From currency: ").strip().upper()
        to_cur=input("To currency: ").strip().upper()
        if from_cur in currency_rates and to_cur in currency_rates:
            usd=amount/currency_rates[from_cur]
            converted=round(usd*currency_rates[to_cur],2)
            print(f"{amount} {from_cur} = {converted} {to_cur}")
        else:
            print("Invalid currency!")
# ================== Unit Conversion ==================
    if choice=='4':
        print("\n--- Unit Conversion ---")
        print("Units: m2cm, cm2m, km2m, m2km, mile2km, km2mile, kg2g, g2kg, lb2kg, kg2lb, l2ml, ml2l")
        val=float(input("Enter value: "))
        unit_type=input("Choose unit conversion: ")
        result=convert_units(val,unit_type)
        print("Result:",result)
# ================== Graph ==================
    if choice=='5':
        print("\n--- Graph ---")
        x_input=input("Enter X values (comma separated): ")
        y_input=input("Enter Y values (comma separated): ")
        x=[float(i) for i in x_input.split(',')]
        y=[float(i) for i in y_input.split(',')]
        plt.plot(x,y,marker='o')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Graph")
        plt.grid(True)
        plt.show()

# ================== XO game ==================
    if choice=='6':
        print("\n--- Play XO ---")
        print("Positions: 0 1 2\n           3 4 5\n           6 7 8")
        board=[' ']*9
        turn='X'
        while True:
            print(f"{board[0]}|{board[1]}|{board[2]}")
            print("-+-+-")
            print(f"{board[3]}|{board[4]}|{board[5]}")
            print("-+-+-")
            print(f"{board[6]}|{board[7]}|{board[8]}")
            move=input(f"{turn}'s turn (0-8): ")
            if not move.isdigit() or int(move) not in range(9) or board[int(move)]!=' ':
                print("Invalid move!")
                continue
            board[int(move)]=turn
            winner=None
            combos=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            for a,b,c in combos:
                if board[a]==board[b]==board[c] and board[a]!=' ':
                    winner=board[a]
                    break
            if winner:
                print(f"{winner} wins!")
                break
            elif ' ' not in board:
                print("It's a draw!")
                break
            if turn=='X':
                turn='O'
            else:
                turn='X'
# ================== Exit ==================
    if choice=='7':
        print("see you later!")
        break
    if choice not in ['1','2','3','4','5','6','7']:
        print("Invalid choice! Please try again.")


