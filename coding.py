from tkinter import *
import tkinter.messagebox

def channelCapacity():
    #matrix
    frame0.pack()

    label = Label(frame0, text="hello,world")
    label.pack()
    print("hello,world")

def uniqueDecodeableCode():
    frame1.pack()

    def onClick():
        str = code.get()
        if str.isdigit():
            for i in range(0, len(str)):
                if (int(str[i]) != 0) and (int(str[i])!= 1):
                    tkinter.messagebox.showinfo("Information", "Please input 0/1 number")
                    break

        else:
            tkinter.messagebox.showinfo("Information", "Please input 0/1 number")

    codeLabel = Label(frame1, text="Please input any code:")
    code = Entry(frame1)
    showLabel1 = Label(frame1, text="Unique Decodeable Code:")
    showLabel2 = Label(frame1, text="Wating calculate...")
    button = Button(frame1, text="confirm", command=onClick)
    codeLabel.grid(row=0, column=0)
    code.grid(row=0, column=1)
    button.grid(row=0, column=2, sticky=E) #sticky 贴合方向W,E,S,N
    showLabel1.grid(row=2, column=0)
    showLabel2.grid(row=2, column=1)

def shannonCoding():
    print("hello,world")

def huffmanCoding():
    print("hello,world")

def fanoCoding():
    print("hello,world")

def LZWCoding():
    print("hello,world")


# 主窗口
root = Tk()               # 主窗口实例化
root.title("coding")      # 主窗口标题
root.geometry("450x200+100+100")  # 主窗口大小
menubar = Menu(root)

fmenu1 = Menu(root)
fmenu1.add_command(label='Channel capacity', command=channelCapacity)
fmenu1.add_command(label='Unique decodable code', command=uniqueDecodeableCode)

fmenu2 = Menu(root)
fmenu2.add_command(label='Shannon Coding', command=shannonCoding)
fmenu2.add_command(label='Huffman Coding', command=huffmanCoding)
fmenu2.add_command(label='Fano Coding', command=fanoCoding)

fmenu3 = Menu(root)
fmenu3.add_command(label='Lempel-Ziv-Welch Coding', command=LZWCoding)
fmenu3.add_command(label='Hammming(7,4)编译码器')

fmenu4 = Menu(root)
fmenu4.add_command(label="MH码")
fmenu4.add_command(label="LZ编码")

menubar.add_cascade(label="基础理论", menu=fmenu1)
menubar.add_cascade(label="信源编码方式", menu=fmenu2)
menubar.add_cascade(label="常用编码", menu=fmenu3)
menubar.add_cascade(label="综合", menu=fmenu4)

#创建frame来解决不同窗口间切换 单击后关闭frame再重新打开
frame0 = Frame(height=450,width=200)
frame1 = Frame(height=450,width=200)
frame2 = Frame(height=450,width=200)
frame3 = Frame(height=450,width=200)
frame4 = Frame(height=450,width=200)
frame5 = Frame(height=450,width=200)
frame6 = Frame(height=450,width=200)
frame7 = Frame(height=450,width=200)
frame8 = Frame(height=450,width=200)
frame9 = Frame(height=450,width=200)


root.config(menu=menubar)
root.mainloop()


'''label = Label(root, text="hello,world")
label.pack()
button = Button(root, text="click me!", command=onclick)
button.pack()'''