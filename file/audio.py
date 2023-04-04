import csv as json
import pandas as pd

def to_dict(d):
    return [dict(row) for row in d]

def dump_json(f, d):
    with open(f, 'w') as f:
        json.dump(d, f)
        
def read_json(f):
    with open(f) as f:
        return json.load()
    
if __name__ == '__main__':
    df = pd.read_csv('audio.csv')
    print(df, '\n')
    data = json.DictReader(open('audio.csv'))
    d = to_dict(data)
    for row in d:
        if(row['pno'][0] not in ['a','c','p','s']):
            if(row['pno'][0] == '8'):
                row['pno'] = 'a' + row['pno']
            elif(row['pno'][0] == '7'):
                row['pno'] = 'p' + row['pno']
            elif(row['pno'][0] == '5'):
                row['pno'] = 's' + row['pno']
            
            if(row['color']) == '-':
                row['color'] = 'silver'
            if row['model'] == '-':
                row['model'] = 'S1'
            if (row['mfg']) == '100':
                row['mfg'] = 'Linn'
            if (row['desc'] == '0') and row['pno'][0] == 'p':
                row['desc'] = 'preamplifier'
            elif (row['desc'] == '-') and row['pno'][0] == 's':
                row['desc'] = 'speakers'
            if (row['price'][0] == '$'):
                row['price'] =\
                row['price'].translate({ord(i): None for i in '$,.'})
        json_file = '/root/Desktop/pythonTest/audio.csv'   
        dump_json(json_file, d)
        data = read_json(json_file)
        for i, row in enumerate(data):
            if i<5:
                print(row)
