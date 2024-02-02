import ui
import dashscope
from http import HTTPStatus
from zhipuai import ZhipuAI


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: ui

    def __init__(self):
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
        # self.initDefaultApiKey()

    def sendZhipu(self, evt):
        zhipu_api_key = self.ui.tk_input_zhipu_api_key_input.get()
        user_input = self.ui.tk_text_zhipu_prompt_text.get("1.0", "end")
        mode_name = self.ui.tk_select_box_zhipu_model_select.get()
        top_p = self.ui.tk_input_zhipu_top_p_input.get()
        temperature = self.ui.tk_input_zhipu_temperature_input.get()

        self.ui.tk_text_zhipu_result_text.delete("1.0", 'end')  # 清空文本框内容
        try:
            client = ZhipuAI(api_key=zhipu_api_key)  # 请填写您自己的APIKey

            response = client.chat.completions.create(
                model=mode_name,  # 填写需要调用的模型名称
                messages=[
                    # {"role": "system", "content": "请根据我的描述回答问题"},
                    {"role": "user",
                     "content": user_input}
                ],
                stream=True,
                top_p=top_p,
                temperature=temperature,
            )
            for chunk in response:
                self.ui.tk_text_zhipu_result_text.insert('end', chunk.choices[0].delta.content)  # 将结果写入文本框
                self.ui.tk_text_zhipu_result_text.update()  # 更新写入
        except Exception as e:
            out_content = e
            self.ui.tk_text_zhipu_result_text.insert('end', out_content)  # 将结果写入文本框

    def sendQwen(self, evt):
        dashscope.api_key = self.ui.tk_input_qwen_api_key_input.get()
        user_input = self.ui.tk_text_qwen_prompt_text.get("1.0", "end")
        mode_name = self.ui.tk_select_box_qwen_model_select.get()
        top_p = self.ui.tk_input_qwen_top_p_input.get()
        temperature = self.ui.tk_input_qwen_temperature_input.get()

        response_generator = dashscope.Generation.call(
            model=mode_name,
            prompt=user_input,
            top_p=top_p,
            temperature=temperature,
            stream=True,
        )

        for response in response_generator:
            self.ui.tk_text_qwen_result_text.delete("1.0", 'end')  # 清空文本框内容
            if response.status_code == HTTPStatus.OK:
                out_content = response.output
                self.ui.tk_text_qwen_result_text.insert('end', out_content.text)  # 将结果写入文本框
                self.ui.tk_text_zhipu_result_text.update()  # 更新写入
            else:
                self.ui.tk_text_qwen_result_text.insert('end', response)  # 将结果写入文本框
                self.ui.tk_text_zhipu_result_text.update()  # 更新写入

    def switchTabDo(self, evt):
        tab_index = self.ui.tk_tabs_llm.select()
        if tab_index == 0:  # 智谱
            self.ui.tk_input_zhipu_api_key_input.focus_set()
        else:
            self.ui.tk_input_qwen_api_key_input.focus_set()
