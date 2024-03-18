#Christopher DeTullio
#CS175L
#AverageFromInput
def main():
    numbers = []
    with open("/Users/chrisdetullio314/Downloads/numbers.txt") as file:
        for i, line in enumerate(file, 1):
            numbers.append(float(line.strip()))
            print("I read in", i, "number(s). Current number is:", line.strip())
    average = sum(numbers) / len(numbers)
    print("Average:", average)
if __name__ == '__main__':
    main()
