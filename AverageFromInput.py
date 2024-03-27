#Christopher DeTullio
#CS175L
#AverageFromInput

def main():
    total = 0
    try:
        numbers = []
        line_number = 1
        with open("/Users/chrisdetullio314/Downloads/numbers.txt") as file:
            for i, line in enumerate(file, 1):
                try:
                    number = float(line.strip())
                    numbers.append(number)
                    total += number
                    print(f"I read in {line_number} number(s). Current number is: {number:.2f}. Total is: {total:.2f}")
                    line_number += 1
                    
                except ValueError as e:
                    print(f"Bad data: {line.strip()} skipping")

        if numbers:
            average = sum(numbers) / len(numbers)
            print("Average:", average)
            
        else:
            print("There are no numbers in this file.")

    except IOError as e:
        print(f"SystemExit: File not found: '{e.filename}' - exiting")
   
if __name__ == '__main__':
    main()
