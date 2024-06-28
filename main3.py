from gtts import gTTS

txt = "안녕하세요. 근명고등학교 홍길동입니다."
tts = gTTS(text=txt, lang='ko')
tts.save("hi.mp3")