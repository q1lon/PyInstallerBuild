import os
# 导入布局文件
from ui import Win as MainWin
# 导入窗口控制器
from control import Controller as MainUIController

# os.environ['TK_SILENCE_DEPRECATION'] = '1'
# 将窗口控制器 传递给UI
app = MainWin(MainUIController())

if __name__ == "__main__":
    # import platform
    # arch = platform.machine()
    # print(f"当前系统架构为：{arch}")

    # 启动
    app.mainloop()

