import pandas as pd
from reviewanalysis.apple_review import AppReview

if __name__=="__main__":
    ap = AppReview("us", "kardia")
    df = ap.get_reviews(num_reviews=20)
    ap.generate_embeddings()
    ap.cluster_embeddings(num_topics=10)
    ap.plot_embeddings(port_num=9050)