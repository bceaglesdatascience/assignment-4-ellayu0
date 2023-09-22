def add_tax(costs, tax_rate):
    taxed_costs = []
    for cost in costs:
        taxed_cost = cost * (1 + tax_rate)
        taxed_costs.append(taxed_cost)
    return taxed_costs

customer_names = []
item_costs = []

num_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

for _ in range(num_purchases):
    customer_name = input("Customer: ")
    cost = float(input("Cost: "))
    
    customer_names.append(customer_name)
    item_costs.append(cost)

taxed_costs = add_tax(item_costs, sales_tax)

customer_totals = {}

for i in range(num_purchases):
    customer_name = customer_names[i]
    cost_with_tax = taxed_costs[i]
    
    if customer_name in customer_totals:
        customer_totals[customer_name] += cost_with_tax
    else:
        customer_totals[customer_name] = cost_with_tax

print(customer_totals)
