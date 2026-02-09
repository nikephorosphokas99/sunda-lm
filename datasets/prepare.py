
import os
import re

path = os.getcwd() + "/text-wiki-dataset"
print(path)
files = os.listdir(path)

texts = ""
for content in files[:100]:

    with open(os.path.join(path, content), 'r', encoding='utf-8') as file:
        text = file.read()
        # print(text)      

        text = re.sub(r'</doc>', "", text)
        texts += "\n".join(text.split('\n'))


    
    # break
print(texts)