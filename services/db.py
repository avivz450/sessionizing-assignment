import pandas as pd

class DB:
    SESSIONS_PATH = './data/final_result.csv'
    __instance = None

    @staticmethod
    def get_instance():
        if DB.__instance is None:
            DB.__instance = DB()
        return DB.__instance

    def __init__(self):
        if DB.__instance is not None:
            raise Exception("DB classes are not supposed to be instantiated more than once.")

    def init_db(self):
        df = pd.read_csv(self.SESSIONS_PATH, header=None)
        self.query_1_dict = df.groupby(1)[0].count().to_dict();
        self.query_2_dict = df.groupby(1)[0].median().to_dict();
        self.query_3_dict = df.groupby(2)[1].nunique().to_dict();
        pass

    def get_num_of_sessions_by_site_url(self, site_url):
        return str(self.query_1_dict[site_url])

    def get_sessions_length_median(self, site_url):
        return str(self.query_2_dict[site_url])

    def get_num_of_unique_visited_sites(self, visitor_id):
        return str(self.query_3_dict[visitor_id])