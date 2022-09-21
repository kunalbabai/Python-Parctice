#importing the dependecies
from newspaper import Article
import nltk
from gtts import gTTS
def text_speech(path,data,language):
    try:
        path = r"{}".format(path)
        article_text = Article(data)
        article_text.download()
        article_text.parse()
        #nltk.download('punkt')
        article_text.nlp()
        #Get the articles text
        article_text = article_text.text
        #now creating goole text to voce api object
        myobj = gTTS(text=article_text,lang=language,slow=False)
        #"I am Kunal Seth & My Father Name is Gobinda Chandra Seth. I'm from West Bengal India"
        #saving the audio file
        myobj.save(path+".mp3")
        print(f"File Converted sucessfully!!!!! -> {path} check this path")
    except Exception:
        return Exception
text_speech(path="E:",data="https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx",language='en')
