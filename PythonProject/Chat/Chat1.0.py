import openai
from PIL import Image
import requests
from io import BytesIO

# 设置 API 密钥
openai.api_key = " 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"

model_engine = "text-davinci-003"# 对话模型的名称
temperature = 0.5  # 值在[0,1]之间，越大表示回复越具有不确定性
max_tokens = 1200  # 回复最大的字符数
top_p = 1
frequency_penalty = 0  # [-2,2]之间，该值越大则更倾向于产生不同的内容
presence_penalty = 0  # [-2,2]之间，该值越大则更倾向于产生不同的内容

def chatText():
    while True:
        prompt = input("请输入你的问题：")
        # 设置请求参数
        # 发送请求
        if prompt[0]=="画":
            response = openai.Image.create(
                prompt=prompt,  # 图片描述
                n=1,  # 每次生成图片的数量
                size="512x512"  # 图片大小,可选有 256x256, 512x512, 1024x1024
            )
            image_url = response['data'][0]['url']
            imageRes=requests.get(image_url)
            image=Image.open(BytesIO(imageRes.content))
            image.show()
        else:
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty
            )

            # 解析响应结果
            print(response.choices[0].text)

chatText()