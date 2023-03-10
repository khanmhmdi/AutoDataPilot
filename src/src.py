import pandas as pd 
import numpy as np 

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


    def remove_nan_values_chunked(df, chunk_size=1000):
        # Replace all NaN values with None
        df = df.where(pd.notnull(df), None)
        
        # Split the dataframe into chunks
        chunks = pd.read_csv(df, chunksize=chunk_size)
        
        # Create an empty list to store the filtered chunks
        filtered_chunks = []
        
        # Process each chunk
        for chunk in chunks:
            # Drop any rows with missing values
            chunk = chunk.dropna()
            
            # Append the filtered chunk to the list
            filtered_chunks.append(chunk)
        
        # Concatenate the filtered chunks back into a single dataframe
        filtered_df = pd.concat(filtered_chunks)
        
        return filtered_df