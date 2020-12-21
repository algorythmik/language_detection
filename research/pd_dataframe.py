import os
import re

import pandas as pd
import nltk


def process_sentence(sentence):
    """Removes all special characters from sentence. It will also strip out
    extra whitespace and makes the string lowercase.
    """
    return re.sub(r'[\\\\/:*«`\'?¿";!<>,.|]', "", sentence.lower().strip())


# def split_into_sentences(file_opj):

#         for line in file_opj:
#             splits = line.split(".")
#             if len(splits) > 1:
#                 sentence, remainder = splits[0], splits[1:]
#             else:
#                 reminder = splits


sent_tokenizer = {
    "da": nltk.data.load("tokenizers/punkt/danish.pickle"),
    "no": nltk.data.load("tokenizers/punkt/danish.pickle"),
    "se": nltk.data.load("tokenizers/punkt/swedish.pickle"),
}

dfs = []
for lan in ["da", "no"]:
    print(lan)
    file_path = os.path.join(f"./data/{lan}_output.txt")
    with open(file_path, "r") as f:
        sentences = sent_tokenizer[lan].tokenize(f.read())
        df_lan = pd.DataFrame(
            ({"text": sentence, "lan": lan} for sentence in sentences)
        )

    dfs.append(df_lan)

df = pd.concat(dfs)
# del dfs
# del df_lan
df["text"] = df["text"].apply(process_sentence)

df.to_pickle(os.path.join("data", "processed", "df_all.pkl"))
