from pathlib import Path

def vocab_parser(dir):
    vocab_dict = {}

    for path in Path(dir).rglob("*"):
        if path.is_file():
            vocab_dict[path.stem] = str(path)

    return vocab_dict

voice = "Standard Voice"

vocab = vocab_parser(f"./defect-detector/Vocabulary/{voice}")
for item in vocab:
    print(item + "|" + vocab[item])