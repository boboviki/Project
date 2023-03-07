from tkinter import *  # 导入tkinter库


class gui:  # 定义class类，GUI界面

    # __init__方法，导入类时自动执行这里的语句
    def __init__(self, x=100, y=100):
        self.xr = 100
        self.yr = 100

        # 主题的字典
        self.colorthemes = {"yellow": ["#FFFACD", "#F0E68C"],
                            "blue": ["#98F5FF", "#00E5EE"],
                            "red": ["#E9967A", "#EE6363"],
                            "green": ["#90ee90", "#32CD32"]
                            }

        self.setgui(x, y)  # 调用self.setgui()方法做GUI界面

    # GUI界面
    def setgui(self, x, y):
        self.root = Tk()  # 窗口
        self.root.title('ydm')  # 窗口标题
        self.root.geometry('200x200+{0}+{1}'.format(x, y))  # 改变窗口位置
        self.root.wm_attributes("-topmost", True)  # 窗口总在最前
        self.root.overrideredirect(True)  # 窗口去边框

        self.themecolor = list(self.colorthemes.values())[0]  # 获取主题名

        # 标题栏
        self.titleframe = Frame(self.root, bg=self.themecolor[0], bd=0)
        self.titleframe.grid(row=0, column=0, sticky='nswe')

        # 拖动窗体的按钮
        self.icon = Label(self.titleframe, text='Ｎ', font=('宋体', 10), cursor='fleur', anchor='center',
                          bg=self.themecolor[0])
        self.icon.grid(row=0, column=0, sticky='nswe')
        # 绑定拖动事件
        self.icon.bind('<ButtonPress-1>', self.setxy)
        self.icon.bind('<B1-Motion>', self.resize)

        # 标题
        self.title = Entry(self.titleframe, font=("微软雅黑", 10), bd=0, bg=self.themecolor[0])
        self.title.grid(row=0, column=1, sticky='nswe')
        self.title.insert(0, '小有有的便签')

        # 设置按钮
        self.sets = Label(self.titleframe, text='…', font=("宋体", 10), anchor='center', bg=self.themecolor[0])
        self.sets.grid(row=0, column=3, sticky='nswe')
        # 绑定单击事件，调用self.postsetsmenu()方法弹出菜单
        self.sets.bind('<ButtonRelease-1>', self.postsetsmenu)

        # 关闭按钮
        self.quit = Label(self.titleframe, text='×', font=("宋体", 10), anchor='center', bg=self.themecolor[0])
        self.quit.grid(row=0, column=4, sticky='nswe')
        # 绑定单击事件，调用self.quitapp()方法卸载窗体
        self.quit.bind('<ButtonRelease-1>', self.quitapp)

        # 文本区域
        self.text = Text(self.root, font=("微软雅黑", 10), bd=0, bg=self.themecolor[0])
        self.text.grid(row=1, column=0, sticky='nswe')

        # 给所有组件绑定鼠标进入、离开事件
        self.root.bind_all('<Enter>', self.enter)
        self.root.bind_all('<Leave>', self.leave)

        # 设置填充
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.titleframe.grid_columnconfigure(1, weight=1)

        # 颜色主题菜单的绑定变量
        self.themesvar = IntVar()
        self.themesvar.set(0)

        # 创建菜单
        self.setsmenu = Menu(self.root, tearoff=False)
        self.setsmenu.add_command(label='新建', command=lambda: gui(x=self.root.winfo_x() + self.root.winfo_width() + 10,
                                                                  y=self.root.winfo_y()))  # 实例化新的gui，新建一个窗口
        self.setsmenu.add_cascade(label='保存', command=lambda: self.save(name=self.title.get(), text=self.text.get(1.0,
                                                                                                                  'end')))  # 调用self.save()方法保存文件

        self.setsmenu.add_separator()  # 添加分隔线

        # 颜色主题菜单
        self.themesmenu = Menu(self.setsmenu, tearoff=False)
        for i in range(len(self.colorthemes.keys())):
            self.themesmenu.add_radiobutton(label=list(self.colorthemes.keys())[i], variable=self.themesvar, value=i,
                                            command=self.setcolor)  # 调用self.setcolor()方法设置所有组件的颜色
        self.setsmenu.add_cascade(label='颜色主题', menu=self.themesmenu)

        self.root.mainloop()  # 窗体进入事件循环

    # 鼠标进入组件事件
    def enter(self, event):
        event.widget['bg'] = list(self.colorthemes.values())[self.themesvar.get()][1]  # 背景颜色改变

    # 鼠标离开组件事件
    def leave(self, event):
        event.widget['bg'] = list(self.colorthemes.values())[self.themesvar.get()][0]  # 背景颜色还原

    # 下面两个为窗体移动的方法
    def setxy(self, event):
        self.xr = event.x
        self.yr = event.y

    def resize(self, event):
        self.root.geometry(
            '+{0}+{1}'.format(self.root.winfo_x() + event.x - self.xr, self.root.winfo_y() + event.y - self.yr))

    # 点击菜单的颜色选项后，设置所有组件的颜色
    def setcolor(self):
        self.includes = [self.titleframe, self.icon, self.title, self.sets, self.quit, self.text]  # 列出所有组件
        for r in self.includes:
            r.configure(bg=list(self.colorthemes.values())[self.themesvar.get()][0])  # 设置组件的颜色

    # 弹出设置菜单
    def postsetsmenu(self, event):
        self.setsmenu.post(event.x_root, event.y_root)

    # 保存文件
    def save(self, name, text):
        # 以标题命名保存文件
        with open('notes/{0}.txt'.format(name), 'w') as f:
            f.write(text)  # 写入文件

    # 卸载窗体
    def quitapp(self, event):
        self.root.destroy()


if __name__ == '__main__':
    gui(x=100, y=100)  # 实例化gui