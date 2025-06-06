import pandas as pd
dictionary = {
    'students': ['sami', 'ovi', 'proyash', 'fatir'],
    'score': [23, 26, 23, 24]
}
data=pd.DataFrame(dictionary)
data.to_csv("Pandas/score.csv")
