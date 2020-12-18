import csv
import pandas as pd

def generate_csv(input_df, csv_path, num_topics):
    topic_dict = {'Topic {}'.format(i) for i in range(num_topics)}
    for idx, i in enumerate(input_df['label']):
        topic_dict['Topic {}'.format(i)].append(input_df['text'][idx])

    keys = sorted(topic_dict)
    with open(csv_path, "wb") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(keys)
        writer.writerows(zip(*[topic_dict[key] for key in keys]))
