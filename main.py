'''
You work for a casino.  It is the law that all transactions over $10,000 must be filed with the federal government.
One of your repsonsibilities is to review recent tansaction history and write the reports needed to file those
transactions with the government.

Your other repsonsibilities include writing a daily transactions report
    - total number of transactions
    - number of cash ins, and cash outs
    - net profit / loss
    - Top spenders (anyone who spent over 100,000) 
    - time vs transactions graph

1) create a daily over $10,000 report
    - date, time, guest, amount

2) create a daily transaction report
    - total number of transactions, cash in vs cash out, profit/loss, top spenders

3) create a time vs transactions graph

4) being the lazy programmers we are, automate this.

5) print out and hand in the reports
'''

#import libraries
import csv


def write_to_csv(data:list, headers:list, path:str)->None:
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def read_csv(filepath:str)->list:
    data=[]
    with open(filepath, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def main():
    #1 import data
    transactions = read_csv('transactions/2024-05-14.csv')
    users = read_csv('users/users.csv')

    over_10k = []
    for transaction in transactions:
        if float(transaction.get('transaction')) >= 10000.00:
            over_10k.append(transaction)

    

    #2 filter out transactions over 10k

    #3 match transactions to users
    for item in over_10k:
        id = item.get('user')
        user = [user for user in users if user.get('id') == id][0]
        item['user'] = user

    #4 write to csv
    headers = ['date', 'guest', 'amount']
    data = []
    for item in over_10k:
        data.append({
            'date' : item.get('timestamp'),
            'guest' : item.get('user').get('first_name') + ' ' + item.get('user').get('last_name'),
            'amount' : item.get('transaction')
        })

    for d in data:
        print(d)
if __name__ == "__main__":
    main()
