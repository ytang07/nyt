# uncomment the two lines below to call summarizer
# from request_layer import summarize_headlines
# summarize_headlines(2021, 10)
import json

from archive import month_dict

# now let's explore our summarized content
def explore_summarized(year, month):
    filename = f"{year}/{month_dict[month]}_Summary.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
    except:
        raise NameError("No Such File")
    
    modded = []
    for entry in entries:
        new = entry.replace(" .", "")
        modded.append(new)
    return " ".join(modded)


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
def wordcloud(year, month):
    headlines = explore_summarized(year, month) # expects a string
    stopwords = set(STOPWORDS)
    frame_mask=np.array(Image.open("R.png"))
    wordcloud = WordCloud(mask=frame_mask, stopwords=stopwords, background_color="white").generate(headlines)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

wordcloud(2021, 10)

# make sure white pixels are 255
# frame_mask=np.array(Image.open("R.png"))
# print(frame_mask)