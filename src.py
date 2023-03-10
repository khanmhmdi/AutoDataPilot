class Data:
    def __init__(self, PATH, chunk_size=10000 , RAM_SIZE = 4):
        self.PATH = PATH
        self.chunk_size = chunk_size
        self.RAM_SIZE = 4
    
    def read_data(self):
        df = pd.DataFrame()
        for chunk in pd.read_csv(self.PATH, chunksize=self.chunk_size):
            #TO_DO
            df = pd.concat([df, chunk])
        print(df.head())