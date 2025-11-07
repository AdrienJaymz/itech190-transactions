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

def write_daily_over_10k_report(transactions:list, users:list, file:str):

    #filter out transactions over 10k
    over_10k = []
    for transaction in transactions:
        if float(transaction.get('transaction')) >= 10000.00 or float(transaction.get('transaction')) <= - 10000.00:
            over_10k.append(transaction)
  

    #match transactions to users
    for item in over_10k:
        id = item.get('user')
        user = [user for user in users if user.get('id') == id][0]
        item['user'] = user


    #write to csv
    headers = ['date', 'guest', 'amount']
    data = []
    for item in over_10k:
        data.append({
            'date' : item.get('timestamp'),
            'guest' : item.get('user').get('first_name') + ' ' + item.get('user').get('last_name'),
            'amount' : item.get('transaction')
        })

    write_to_csv(data, headers, f"reports/{file}.csv")

def get_total_num_transactions(transactions:list)->int:
    return len(transactions)

def get_sum_of_transactions(transactions:list)->float:
    return sum(transactions)

def get_avg_of_transactions(transactions:list)->float:
    return sum(transactions) /len(transactions)

def get_cash_in_out_report(transactions:list)->dict:
    positive = [float(transaction.get('transaction')) for transaction in transactions if float(transaction.get('transaction')) >=0]
    negative = [float(transaction.get('transaction')) for transaction in transactions if float(transaction.get('transaction')) <0]
    net = [float(transaction.get('transaction')) for transaction in transactions]
    return{
        "number_transactions_positive": get_total_num_transactions(positive),
        "sum_transactions_positive": get_sum_of_transactions(positive),
        "average_transactions_positive": get_avg_of_transactions(positive),
        "number_transactions_negative": get_total_num_transactions(negative),
        "sum_transactions_negative": get_sum_of_transactions(negative),
        "average_transactions_negative": get_avg_of_transactions(negative),
        "number_transactions_net": get_total_num_transactions(net),
        "sum_transactions_net": get_sum_of_transactions(net),
        "average_transactions_net": get_avg_of_transactions(net),
    }
    


def main():
    #1 import data

    transactions = read_csv('transactions/2024-05-14.csv')
    users = read_csv('users/users.csv')
    
    #over 10k report
    #write_daily_over_10k_report(transactions, users,'2024-05-14-2')

    #get total number of transactions
    #total = get_total_num_transactions(transactions)
    #print(f"total transactions: {total}")

    #cash in cash out
    #in_total, in_len, in_avg, out, net
    cash_in_out_report = get_cash_in_out_report(transactions)
    for key,val in cash_in_out_report.items():
        print(key, val)

if __name__ == "__main__":
    main()
