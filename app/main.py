def main() -> None:
    file_name = input("Enter the name of the data file: ")

    with open(file_name + ".txt", "w") as new_file:
        while True:
            user_input = input(
                "Enter data to write to the file (or type 'exit' to stop): "
            )

            if user_input == "exit":
                break

            new_file.write(user_input + "\n")


if __name__ == "__main__":
    main()
