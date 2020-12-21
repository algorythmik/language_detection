import os
import argparse
from gensim.corpora import WikiCorpus
import tqdm


def tokenize(content, token_min_len=1, token_max_len=15, lower=True):
    res = []
    for token in content.split():
        if token_min_len <= len(token) <= token_max_len:
            if (
                token.startswith("_")
                or token.startswith("'''")
                or token.startswith("**")
                or token.startswith("==")
            ):
                continue
            res.append(lower(token))
    return res


def convert_wiki_dump_to_txt(input_file, output_file):
    """Converts Wikipedia xml dump file to text corpus."""

    with open(output_file, "w") as out_f:
        wiki = WikiCorpus(input_file, tokenizer_func=tokenize)

        for text in tqdm.tqdm(wiki.get_texts()):
            out_f.write(bytes(" ".join(text), "utf-8").decode("utf-8") + "\n")

    print("Conversion completed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="choose language for conversion.")
    parser.add_argument("lan", choices=["da", "se", "no"])
    lan = parser.parse_args().lan

    input_file = os.path.join(
        "data", f"{lan}wiki-20200720-pages-articles-multistream.xml.bz2"
    )
    output_file = os.path.join("data", f"{lan}_output.txt")
    convert_wiki_dump_to_txt(input_file, output_file)
