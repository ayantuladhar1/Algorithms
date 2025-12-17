# Name: Ayan Tuladhar
# Student ID: 109974948


# Read all the references of REST and Web API.  Say Yes if you did (2 points)
# - counted only if you implemented at least up to step 2.

# Yes, I DID and the implementation is represented below.

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import string
with open('test.txt',encoding="utf8") as f:
    characters = f.read()
    alphabets = characters.split()
    metrics = str.maketrans("", "", string.punctuation)
    extra = [w.translate (metrics) for w in alphabets]
    combined = " ".join(extra)


wc = WordCloud(background_color = "black", contour_color = "steelred")
wc.generate(combined)
plt.imshow(wc, interpolation= "bilinear")
plt.show()
