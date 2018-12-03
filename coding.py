from tkinter import *

# 主窗口
root = Tk()               # 主窗口实例化
root.title("coding")      # 主窗口标题
root.geometry("700x400")  # 主窗口大小(700x400)及起始位置(100,100),以像素为单位

#菜单栏
def menu():
    menubar = Menu(root)

    fmenu1 = Menu(root)
    for item in ['信道容量', '唯一可译码判断准则']:
        # 如果该菜单是顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
        fmenu1.add_command(label=item)

    fmenu2 = Menu(root)
    for item in ['香农编码', '霍夫曼编码', '费诺编码']:
        fmenu2.add_command(label=item)

    fmenu3 = Menu(root)
    for item in ['LZW编码', 'Hammming(7,4)编译码器']:
        fmenu3.add_command(label=item)

    fmenu4 = Menu(root)
    for item in ["MH码", "LZ编码"]:
        fmenu4.add_command(label=item)

    menubar.add_cascade(label="基础理论", menu=fmenu1)
    menubar.add_cascade(label="信源编码方式", menu=fmenu2)
    menubar.add_cascade(label="常用编码", menu=fmenu3)
    menubar.add_cascade(label="综合", menu=fmenu4)

    root.config(menu=menubar)


menu()
root.mainloop()                     # 主窗口运行