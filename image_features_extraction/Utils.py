
import numpy as np

def insert_values(feature_name, df, values):
    if feature_name =='centroid':
        a = np.array(values)
        x=[]
        y=[]
        for i in a:
            x.append(i[0])
            y.append(i[1])
        df['centroid_x'] = x
        df['centroid_y'] = y
        return 1

    df[feature_name] = values
    return 0
