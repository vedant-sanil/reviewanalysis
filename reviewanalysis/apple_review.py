import pandas as pd

from datetime import datetime
from app_store_scraper import AppStore 
from reviewanalysis.modeller import TopicModeller
from reviewanalysis.utils.csvtools import generate_csv

class AppReview(TopicModeller):
    def __init__(self, country, app_name):
        self.country = country
        self.app_name = app_name
        self.review_unit = AppStore(country=country, app_name=app_name)

        self.topic_reviews = pd.DataFrame()

    def get_reviews(self, num_reviews=None):
        '''
            Returns the reviews as a pandas 
            dataframe.
        '''
        review_dict = {'title':[],
                       'rating':[],
                       'userName':[],
                       'review':[],
                       'date':[],
                       'isEdited':[]}
        if num_reviews:
            self.review_unit.review(how_many=num_reviews)
        else:
            self.review_unit.review()

        for review in self.review_unit.reviews:
            review_dict['title'].append(review['title'])
            review_dict['rating'].append(review['rating'])
            review_dict['userName'].append(review['userName'])
            review_dict['review'].append(review['review'])
            review_dict['date'].append(review['date'].strftime("%m/%d/%Y, %H:%M:%S"))
            review_dict['isEdited'].append(review['isEdited'])

        self.review_df = pd.DataFrame(data=review_dict)

        return self.review_df        

    def generate_embeddings(self):
        '''
            Generates embeddings based on 
            reviews from app store
        '''
        df_dict = {'sentence': []}
        for idx, c in enumerate(self.review_df.review):
            df_dict['sentence'].append(c)

        df_pd = pd.DataFrame(data=df_dict)

        super().__init__(df_pd)

    def cluster_embeddings(self, num_topics=None):
        self.num_topics = num_topics
        self.topic_reviews = super().project(topics=num_topics)

    def plot_embeddings(self, port_num=9000):
        super().plot(self.app_name, port_num=port_num)

    def generate_topic_csv(self, csv_path):
        generate_csv(self.topic_reviews, csv_path, self.num_topics)