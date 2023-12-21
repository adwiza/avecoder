import csv

# print(csv.list_dialects())


def reader_sample():
    with open("../data/Daily_Demand_Forecasting_Orders.csv") as df:
        reader = csv.reader(df)
        for row in reader:
            print(row)


# reader_sample()


def sniffer():
    with open("../data/Daily_Demand_Forecasting_Orders.csv") as snif:
        dialect = csv.Sniffer().sniff(snif.read(1024), delimiters=',')
        snif.seek(0)
        has_header = csv.Sniffer().has_header(snif.read(1024))
        snif.seek(0)
        print("Headers: " + str(has_header))
        print(dialect.delimiter)
        print(dialect.escapechar)
        print(dialect.quotechar)


sniffer()


def write_data():
    with open("../data/Daily_Demand_Forecasting_Orders.csv", mode="w") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(["Week of the month (first week, second, third,  fourth or fifth week",
                             "Day of the week (Monday to Friday)",
                             "Non-urgent order",
                             "Urgent order",
                             "Order type A",
                             "Order type B",
                             "Order type C",
                             "Fiscal sector orders",
                             "Orders from the traffic controller sector",
                             "Banking orders (1)",
                             "Banking orders (2)",
                             "Banking orders (3)",
                             "Target (Total orders)"])
        csv_writer.writerow(
            ["1", "6", "43.651", "84.375", "21.826", "25.125", "82.461", "1.386", "11992", "3452", "21305", "14947",
             "129.412"]
            )


write_data()
