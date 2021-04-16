from result_ordering import divide_by_polarity_and_subjectivity
from preprocessing import preprocess_target
from similarity_calculation_bert import SimilarityTransformer

import pandas as pd


def main(url):

    target_clean, publication_date = preprocess_target(url) # TODO factor date

    print(target_clean)

    transformer = SimilarityTransformer()

    result = transformer.calculate_similarity_for_target(target_clean)

    output = divide_by_polarity_and_subjectivity(result, publication_date, random=False)

    for k, v in output.items():
        if len(v) == 2:
            print(f"{k} :\n {v[0]}\n {v[1]}")
        else:
            print(f"{k} :\n {v[0]}")

    print("OLD")

    print(result.url.iloc[0])
    print(result.url.iloc[1])
    print(result.url.iloc[2])
    print(result.url.iloc[3])
    print(result.url.iloc[4])


if __name__ == '__main__':
    url = "https://www.bbc.com/news/business-56559073"

    main(url)
