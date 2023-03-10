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
    
    def fill_nan_values_chunked(df, fill_type='mean', chunk_size=1000):
        # Split the dataframe into chunks
        chunks = pd.read_csv(df, chunksize=chunk_size)
        
        # Initialize the fill value to None
        fill_value = None
        
        # Find the fill value across all chunks
        for chunk in chunks:
            if fill_type == 'mean':
                chunk_mean = chunk.mean().mean() # Find the mean value in the chunk
                if fill_value is None:
                    fill_value = chunk_mean
                else:
                    fill_value = (fill_value + chunk_mean) / 2 # Compute the running average
            elif fill_type == 'min':
                chunk_min = chunk.min().min() # Find the minimum value in the chunk
                if fill_value is None or chunk_min < fill_value:
                    fill_value = chunk_min
            elif fill_type == 'max':
                chunk_max = chunk.max().max() # Find the maximum value in the chunk
                if fill_value is None or chunk_max > fill_value:
                    fill_value = chunk_max
            else:
                raise ValueError('Invalid fill type: %s' % fill_type)
        
        # Split the dataframe into chunks again
        chunks = pd.read_csv(df, chunksize=chunk_size)
        
        # Create an empty list to store the filled chunks
        filled_chunks = []
        
        # Process each chunk
        for chunk in chunks:
            # Fill any NaN values with the appropriate value
            if fill_type == 'mean':
                filled_chunk = chunk.fillna(fill_value)
            elif fill_type == 'min':
                filled_chunk = chunk.fillna(fill_value)
            elif fill_type == 'max':
                filled_chunk = chunk.fillna(fill_value)
            else:
                raise ValueError('Invalid fill type: %s' % fill_type)
            
            # Append the filled chunk to the list
            filled_chunks.append(filled_chunk)
        
        # Concatenate the filled chunks back into a single dataframe
        filled_df = pd.concat(filled_chunks)
        
        return filled_df
