from utils.WebOperator import Get, Post
from utils.TableOperator import TableOperator
import os

def main():
    get = Get()
    table1 = get.table1
    table2 = get.table2
    to = TableOperator(table1, table2)
    print(f'Tables are now saved to folder {os.path.abspath("temp")}.')
    print(
        """
        Now please modify the CSV files in the temp folder and press "ok" to continue:
        Notice:
        
        1. You can only use English commas!!!!!!
        2. Don't forget to save your changes for the csv files before you press "ok"!!!
        """
    )
    while input("Press 'ok' to continue: ")!= "ok":
        pass
    
    post = Post()
    text = to.merge(get.main_floor)
    data = {
        'title': '【组织部】24-25罚跑及执行通知（理事名单在最后）',
        'text': text,
        'token': get.cookies.get_dict()['token'],
        'icon': '1',
        'bid': '1',
        'tid': '9959',
        'pid': '1',
        'sig': '1',
        'attachs': '',
    }
    post.post(data)


if __name__ == "__main__":
    main()
