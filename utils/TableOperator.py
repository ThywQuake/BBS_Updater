from basic import get_config, table2html
from bs4 import BeautifulSoup

config = get_config()

class TableOperator:
    def __init__(self, table1, table2):
        self.table1 = table1
        self.table2 = table2
    
    def merge(self, context):
        t1soup = BeautifulSoup(table2html(self.table1), 'html.parser')
        t2soup = BeautifulSoup(table2html(self.table2), 'html.parser')
        
        context.find_all("table", class_="contenttable")[0].replace_with(t1soup)
        context.find_all("table", class_="contenttable")[1].replace_with(t2soup)
        
        result = ''
        for c in context.children:
            result += str(c)
            
        return result
        