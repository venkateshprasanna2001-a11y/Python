import pandas as pd
data = {'Batch': ['A', 'B', 'C'], 'Viscosity': [85,130,90]}
df = pd.DataFrame(data)

def check_visc(v):
    if 80<= v <= 120:
        return 'OK'
    else:
            return 'REJECT'
            
df['Status'] = df['Viscosity'].apply(check_visc)

print(df)
