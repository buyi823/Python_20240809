import pyttsx3

# 初始化语音引擎
engine = pyttsx3.init()

# 设置要朗读的文本
text = "Thank you for giving me the opportunity to introduce myself."

# 朗读文本
engine.say(text)

# 等待朗读完成
engine.runAndWait()