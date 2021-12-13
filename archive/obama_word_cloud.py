from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# wordcloud function
def word_cloud(text, title):
    stopwords = set(STOPWORDS)
    frame_mask=np.array(Image.open("cloud_shape.png"))
    wordcloud = WordCloud(max_words=50, mask=frame_mask, stopwords=stopwords, background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis("off")
    plt.show()

for i in list(range(2008, 2018)):
    with open(f"obama/{i}_summary.txt", "r") as f:
        entries = f.readlines()
    
    headlines = "".join(entries)
    word_cloud(headlines, f"Obama {i}")
    