import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

if __name__ == '__main__':
    n = 100
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), num=n)
    y = norm.pdf(x)
    dic = {}
    for i, row in enumerate(y):
      dic[x[i]] = [np.random.uniform(0, row) for _ in range(n)]
    xs = []
    ys = []
    for key, vals in dic.items():
       for y in vals:
           xs.append(key)
           ys.append(y)
    plt.xlim(min(xs), max(xs))
    plt.ylim(0, max(ys)+0.02)
    plt.title('Normal PDF')
    plt.xlabel('x')
    plt.ylabel('Probaility Density')
    plt.scatter(xs, ys, c=xs, cmap='rainbow')
    plt.show()

"""
def str_int(s):
    val = "%.2f" % profit
    return float(val)
    
if __name__ == '__main__':
    orders = [180, 200, 220, 240, 260, 280, 300]
    mu, sigma, n = 200, 30, 10000
    cost,price, discount = 25000, 45000, 30000
    profit_ls = []
    for order in orders:
        x = 1
        profit_val = []
        inv_cost = order * cost
        while x <= n:
            demand = round(np.random.normal(mu,sigma))
            if demand < order:
                diff = order - demand
                if diff > 0:
                    damt = round(abs(diff) / 2) * discount
                    proift = (demand * price) - inv_cost + damt
                else:
                    proift = (order * price) - inv_cost
            else:
                profit = (order * price) - inv_cost
            profit = str_int(profit)
            profit_val.append(profit)
            x += 1
        avg_profit = np.mean(profit_val)
        profit_ls.append(avg_profit)
        print ('${0:,.2f}'.format(avg_profit), '(profit)',
               'for order:', order)
    max_profit = max(profit_ls)
    profit_np = np.array(profit_ls)
    max_ind = np.where(profit_np == profit_np.max())
    print ('\nMaximum profit', '${0:,.2f}'.format(max_profit),'for order', orders[int(max_ind[0])])
    barlist = plt.bar(orders, profit_ls, width=15, color='thistle')
    barlist[int(max_ind[0])].set_color('lime')
    plt.title('Profits by Order Quantity')
    plt.xlabel('orders')
    plt.ylabel('profit')
    plt.tight_layout()
    plt.show()
    
            
"""