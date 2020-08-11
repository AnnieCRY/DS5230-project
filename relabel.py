import pandas as pd

def modify_labels(path):
    csv_file = path + "/labels_BeeNotBee_th0.csv"
    labels_BeeNotBee_th0 = pd.read_csv(csv_file, index_col=0)

    def add_new_labels(df):
        labels_l=[]
        for x in df['label_strength']:
            if x>0.95:
                labels_l.append('nobee') 
            elif x==0:
                labels_l.append('bee') 
            else:
                labels_l.append('unknown') 
        df['label']=labels_l
        return df
    
    labels_BeeNotBee_th0=add_new_labels(labels_BeeNotBee_th0)
    labels_BeeNotBee_th0.to_csv(csv_file, index=False)