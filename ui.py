"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_tabs_llm = self.__tk_tabs_llm(self)
        self.tk_label_qwen_api_key_label = self.__tk_label_qwen_api_key_label(self.tk_tabs_llm_0)
        self.tk_text_qwen_prompt_text = self.__tk_text_qwen_prompt_text(self.tk_tabs_llm_0)
        self.tk_input_qwen_api_key_input = self.__tk_input_qwen_api_key_input(self.tk_tabs_llm_0)
        self.tk_label_qwen_prompt_label = self.__tk_label_qwen_prompt_label(self.tk_tabs_llm_0)
        self.tk_label_qwen_result_label = self.__tk_label_qwen_result_label(self.tk_tabs_llm_0)
        self.tk_text_qwen_result_text = self.__tk_text_qwen_result_text(self.tk_tabs_llm_0)
        self.tk_button_qwen_submit_btn = self.__tk_button_qwen_submit_btn(self.tk_tabs_llm_0)
        self.tk_label_zhipu_api_key_label = self.__tk_label_zhipu_api_key_label(self.tk_tabs_llm_1)
        self.tk_input_zhipu_api_key_input = self.__tk_input_zhipu_api_key_input(self.tk_tabs_llm_1)
        self.tk_text_zhipu_prompt_text = self.__tk_text_zhipu_prompt_text(self.tk_tabs_llm_1)
        self.tk_text_zhipu_result_text = self.__tk_text_zhipu_result_text(self.tk_tabs_llm_1)
        self.tk_button_zhipu_submit_btn = self.__tk_button_zhipu_submit_btn(self.tk_tabs_llm_1)
        self.tk_label_zhipu_prompt_label = self.__tk_label_zhipu_prompt_label(self.tk_tabs_llm_1)
        self.tk_label_zhipu_result_label = self.__tk_label_zhipu_result_label(self.tk_tabs_llm_1)
        self.tk_select_box_zhipu_model_select = self.__tk_select_box_zhipu_model_select(self.tk_tabs_llm_1)
        self.tk_label_zhipu_model_label = self.__tk_label_zhipu_model_label(self.tk_tabs_llm_1)
        self.tk_select_box_qwen_model_select = self.__tk_select_box_qwen_model_select(self.tk_tabs_llm_0)
        self.tk_label_qwen_model_label = self.__tk_label_qwen_model_label(self.tk_tabs_llm_0)
        self.tk_label_qwen_copyright_text = self.__tk_label_qwen_copyright_text(self.tk_tabs_llm_0)
        self.tk_label_zhipu_copyright_text = self.__tk_label_zhipu_copyright_text(self.tk_tabs_llm_1)
        self.tk_label_qwen_top_p_label = self.__tk_label_qwen_top_p_label(self.tk_tabs_llm_0)
        self.tk_input_qwen_top_p_input = self.__tk_input_qwen_top_p_input(self.tk_tabs_llm_0)
        self.tk_label_qwen_temperature_label = self.__tk_label_qwen_temperature_label(self.tk_tabs_llm_0)
        self.tk_input_qwen_temperature_input = self.__tk_input_qwen_temperature_input(self.tk_tabs_llm_0)
        self.tk_label_zhipu_top_p_label = self.__tk_label_zhipu_top_p_label(self.tk_tabs_llm_1)
        self.tk_input_zhipu_top_p_input = self.__tk_input_zhipu_top_p_input(self.tk_tabs_llm_1)
        self.tk_label_zhipu_temperature_label = self.__tk_label_zhipu_temperature_label(self.tk_tabs_llm_1)
        self.tk_input_zhipu_temperature_input = self.__tk_input_zhipu_temperature_input(self.tk_tabs_llm_1)

    def __win(self):
        self.title("LLM Prompt调试助手V0.1.1")
        # 设置窗口大小、居中
        width = 551
        height = 546
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.minsize(width=width, height=height)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_tabs_llm(self, parent):
        frame = Notebook(parent)
        frame.pack()
        self.tk_tabs_llm_0 = self.__tk_frame_llm_0(frame)
        frame.add(self.tk_tabs_llm_0, text="千问")
        self.tk_tabs_llm_1 = self.__tk_frame_llm_1(frame)
        frame.add(self.tk_tabs_llm_1, text="智谱")
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        return frame

    def __tk_frame_llm_0(self, parent):
        frame = Frame(parent)
        frame.pack()
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        return frame

    def __tk_frame_llm_1(self, parent):
        frame = Frame(parent)
        frame.pack()
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        return frame

    def __tk_label_qwen_api_key_label(self, parent):
        label = Label(parent, text="api key", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.03, relwidth=0.10, relheight=0.05)
        return label

    def __tk_text_qwen_prompt_text(self, parent):
        text = Text(parent)
        text.pack()
        text.place(relx=0.04, rely=0.36, relwidth=0.93, relheight=0.18)
        return text

    def __tk_input_qwen_api_key_input(self, parent):
        ipt = Entry(parent, )
        ipt.pack()
        ipt.place(relx=0.04, rely=0.09, relwidth=0.46, relheight=0.05)
        return ipt

    def __tk_label_qwen_prompt_label(self, parent):
        label = Label(parent, text="提示词", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.30, relwidth=0.09, relheight=0.05)
        return label

    def __tk_label_qwen_result_label(self, parent):
        label = Label(parent, text="结果", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.60, relwidth=0.09, relheight=0.05)
        return label

    def __tk_text_qwen_result_text(self, parent):
        text = Text(parent)
        text.pack()
        text.place(relx=0.04, rely=0.66, relwidth=0.93, relheight=0.25)
        return text

    def __tk_button_qwen_submit_btn(self, parent):
        btn = Button(parent, text="提交", takefocus=False, )
        btn.pack()
        btn.place(relx=0.77, rely=0.58, relwidth=0.18, relheight=0.05)
        return btn

    def __tk_label_zhipu_api_key_label(self, parent):
        label = Label(parent, text="api key", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.03, relwidth=0.10, relheight=0.05)
        return label

    def __tk_input_zhipu_api_key_input(self, parent):
        ipt = Entry(parent, )
        ipt.pack()
        ipt.place(relx=0.04, rely=0.09, relwidth=0.46, relheight=0.05)
        return ipt

    def __tk_text_zhipu_prompt_text(self, parent):
        text = Text(parent)
        text.pack()
        text.place(relx=0.04, rely=0.36, relwidth=0.93, relheight=0.18)
        return text

    def __tk_text_zhipu_result_text(self, parent):
        text = Text(parent)
        text.pack()
        text.place(relx=0.04, rely=0.66, relwidth=0.93, relheight=0.25)
        return text

    def __tk_button_zhipu_submit_btn(self, parent):
        btn = Button(parent, text="提交", takefocus=False, )
        btn.pack()
        btn.place(relx=0.77, rely=0.58, relwidth=0.18, relheight=0.05)
        return btn

    def __tk_label_zhipu_prompt_label(self, parent):
        label = Label(parent, text="提示词", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.30, relwidth=0.09, relheight=0.05)
        return label

    def __tk_label_zhipu_result_label(self, parent):
        label = Label(parent, text="结果", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.60, relwidth=0.09, relheight=0.05)
        return label

    def __tk_select_box_zhipu_model_select(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb.pack()
        cb['values'] = ("glm-4", "glm-4v", "glm-3-turbo")
        cb.place(relx=0.54, rely=0.09, relwidth=0.42, relheight=0.06)
        return cb

    def __tk_label_zhipu_model_label(self, parent):
        label = Label(parent, text="model", anchor="center", )
        label.pack()
        label.place(relx=0.54, rely=0.03, relwidth=0.09, relheight=0.05)
        return label

    def __tk_select_box_qwen_model_select(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb.pack()
        cb['values'] = ("qwen-max", "qwen-max-1201", "qwen-max-longcontext", "qwen-plus", "qwen-turbo")
        cb.place(relx=0.54, rely=0.09, relwidth=0.42, relheight=0.06)
        return cb

    def __tk_label_qwen_model_label(self, parent):
        label = Label(parent, text="model", anchor="center", )
        label.pack()
        label.place(relx=0.54, rely=0.03, relwidth=0.09, relheight=0.05)
        return label

    def __tk_label_qwen_copyright_text(self, parent):
        label = Label(parent, text="阿里千问大模型测试©gnway 2024", anchor="center", )
        label.pack()
        label.place(relx=0.00, rely=0.94, relwidth=0.42, relheight=0.05)
        return label

    def __tk_label_zhipu_copyright_text(self, parent):
        label = Label(parent, text="清华智谱大模型测试©gnway 2024", anchor="center", )
        label.pack()
        label.place(relx=0.00, rely=0.94, relwidth=0.42, relheight=0.05)
        return label

    def __tk_label_qwen_top_p_label(self, parent):
        label = Label(parent, text="top_p 范围 0-1", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.17, relwidth=0.19, relheight=0.05)
        return label

    def __tk_input_qwen_top_p_input(self, parent):
        ipt = Entry(parent, )
        ipt.pack()
        ipt.place(relx=0.04, rely=0.23, relwidth=0.46, relheight=0.05)
        return ipt

    def __tk_label_qwen_temperature_label(self, parent):
        label = Label(parent, text="temperature 范围 0-2", anchor="center", )
        label.pack()
        label.place(relx=0.54, rely=0.17, relwidth=0.27, relheight=0.05)
        return label

    def __tk_input_qwen_temperature_input(self, parent):
        ipt = Entry(parent, )
        ipt.pack()
        ipt.place(relx=0.54, rely=0.23, relwidth=0.42, relheight=0.05)
        return ipt

    def __tk_label_zhipu_top_p_label(self, parent):
        label = Label(parent, text="top_p 范围 0-1", anchor="center", )
        label.pack()
        label.place(relx=0.04, rely=0.17, relwidth=0.19, relheight=0.05)
        return label

    def __tk_input_zhipu_top_p_input(self, parent):
        ipt = Entry(parent, )
        ipt.pack()
        ipt.place(relx=0.04, rely=0.23, relwidth=0.46, relheight=0.05)
        return ipt

    def __tk_label_zhipu_temperature_label(self, parent):
        label = Label(parent, text="temperature 范围 0-1", anchor="center", )
        label.pack()
        label.place(relx=0.54, rely=0.17, relwidth=0.27, relheight=0.05)
        return label

    def __tk_input_zhipu_temperature_input(self, parent):
        ipt = Entry(parent, )
        ipt.pack()
        ipt.place(relx=0.54, rely=0.23, relwidth=0.42, relheight=0.05)
        return ipt


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_tabs_llm.bind('<Button-1>', self.ctl.switchTabDo)
        self.tk_button_qwen_submit_btn.bind('<Button-1>', self.ctl.sendQwen)
        self.tk_button_zhipu_submit_btn.bind('<Button-1>', self.ctl.sendZhipu)
        pass

    def __style_config(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
