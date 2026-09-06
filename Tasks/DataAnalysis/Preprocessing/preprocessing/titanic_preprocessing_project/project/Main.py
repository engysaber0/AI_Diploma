from config import config
from preprocessing import Read_data_file, Drop_unnecessary_features, Check_data_type
def main():
    print("Titanic Preprocessing Pipeline")

    df = Read_data_file(config.DATA_FILE_PATH)
    if df is None:
        print("Could not load the data, stopping.")
        return

    while True:
        print("\nWhat do you want to do?")
        print(f"1. Drop columns {config.COLUMNS_TO_DROP}")
        print("2. Check data types")
        print("3. Show current shape")
        print("4. Exit")

        choice = input("Choice (1-4): ").strip()

        if choice == "1":
            df = Drop_unnecessary_features(df, config.COLUMNS_TO_DROP)

        elif choice == "2":
            report = Check_data_type(df)
            print(report)

        elif choice == "3":
            print(df.shape)

        elif choice == "4":
            print("Bye")
            break

        else:
            print("Enter a number from 1 : 4")
if __name__ == "__main__":
    main()
