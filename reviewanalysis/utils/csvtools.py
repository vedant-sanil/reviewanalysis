import csv
import argparse
import pandas as pd

def generate_csv(input_df, csv_path, num_topics):
    ls_df = input_df['text'].tolist()
    topic_dict = {'Topic {}'.format(i) : [] for i in range(num_topics)}
    for idx, i in enumerate(input_df['label']):
        topic_dict['Topic {}'.format(i)].append(ls_df[idx])
    
    max_len = 0
    for key, values in topic_dict.items():
        if len(values) > max_len:
            max_len = len(values)

    for key, values in topic_dict.items():
        values += [''] * (max_len - len(values))
        topic_dict[key] = values

    keys = sorted(topic_dict)
    with open(csv_path, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(keys)
        writer.writerows(zip(*[topic_dict[key] for key in keys]))

