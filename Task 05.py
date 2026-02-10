import pandas as pd

data = {
    'part' : ['Shaft', 'Rotor', 'Pin'],
    'Diameter' : [25.2, 26.5, 24.8]    
}

df = pd.DataFrame(data)

def quality_check(d):
    if 24 <= d <= 26:
        return 'PASS'
    else:
        return 'FAIL'

df['Status'] = df['Diameter'].apply(quality_check)

print(df)
print("-" * 20)

print(df['Status'].value_counts())
