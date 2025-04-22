import toml 
import csv
from io import StringIO
import webbrowser
import os
import re

def get_config():
    try:
        with open('params.toml', 'r') as f:
            config = toml.load(f)
            return config
    except FileNotFoundError:
        print('config.toml not found')
        return None
    
def derive_data(table, path):
    thead = table.find("thead")
    th_texts = []
    for th in thead.find_all("th"):
        th_texts.append(th.text.strip())
    
    tbody = table.find_all("tbody")
    trss = [tb.find_all("tr") for tb in tbody]
    data = []
    for trs in trss:
        for tr in trs:
            tds = tr.find_all("td")
            row = []
            for td in tds:
                row.append(td.text.strip())
            data.append(row)
    csv_table = ""
    csv_table += ",".join(th_texts) + "\n"
    for row in data:
        csv_table += ",".join(row) + "\n"
        
    with open(path, "w") as f:
        f.write(csv_table)
    
    return csv.reader(StringIO(csv_table))

def validate_post(data):
    # assert type(data) is dict, "data should be a dictionary"
    # assert set(data.keys()) == set(
    #     ['title', 'text', 'token', 'icon', 'bid', 'tid', 'pid', 'sig', 'attachs']
    # ), "data should have the following keys: title, text, token, icon, bid, tid, pid, sig, attachs"
    
    with open('page/example.html','r') as f:
        example = f.read()
    content = re.sub(
        r'<div class="textblock" id="floor0" style="line-height:160% !important">(.*)<div class="sigblock">',
        data['text'],
        example,
        flags=re.S
    )
    
    with open('temp/updated_post.html', 'w') as f:
        f.write(content)
    
    path = os.path.abspath('temp/updated_post.html')
    webbrowser.open('file://' + path)
    
if __name__ == '__main__':
    validate_post({'text':'test!'})