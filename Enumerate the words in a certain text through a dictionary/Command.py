from itertools import groupby

text = pd.read_csv("GPL96-15653_clean_version.txt")
text = text.values
col2 = list(text[:,1])
freqs = {key: len(list(phrase)) for key, phrase in groupby(col2)}
print(freqs)
