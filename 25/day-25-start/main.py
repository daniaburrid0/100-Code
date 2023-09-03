import pandas


def main():
    squirrel_df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    squirrel_count = squirrel_df["Primary Fur Color"].value_counts()
    print(squirrel_count)
    squirrel_count.to_csv("squirrel_count.csv")
            
if __name__ == "__main__":
    main()