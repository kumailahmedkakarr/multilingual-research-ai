from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "intfloat/multilingual-e5-large"
)

def embed(text):

    return model.encode(text)