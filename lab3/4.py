import json

firm_profit = {}
profits = []

with open("firms.txt", 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()

        data = list(filter(None, line.split()))

        try:
            name = data[0]
            revenue = float(data[2])
            costs = float(data[3])

            profit = revenue - costs
            firm_profit[name] = profit

            if profit > 0:
                profits.append(profit)

        except (ValueError, IndexError):
           continue

average_profit = sum(profits) / len(profits) if profits else 0
result_list = [firm_profit, {"average_profit": round(average_profit, 2)}]

with open("firms_result.json", 'w', encoding='utf-8') as json_file:
    json.dump(result_list, json_file, ensure_ascii=False, indent=4)

print("Результат:", result_list)