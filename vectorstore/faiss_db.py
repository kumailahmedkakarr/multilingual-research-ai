import faiss
import numpy as np

index = faiss.IndexFlatL2(1024)

def add_vector(vec):

    index.add(
        np.array([vec]).astype("float32")
    )

def search(vec):

    D, I = index.search(
        np.array([vec]).astype("float32"),
        5
    )

    return I