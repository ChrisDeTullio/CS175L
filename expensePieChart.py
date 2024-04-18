import matplotlib.pyplot as plt


def main():
    
    filename = 'expenses.txt'
    expenses = {}
    try:
        with open(r'C:\Users\Christopher DeTullio\Downloads\expenses.txt', 'r') as file:
            for line in file:
                try:
                    label, value = line.strip().split('\t')
                    expenses[label] = int(value)
                except ValueError:
                    print(f"Error: Unable to convert value to integer in line: {line.strip()}")
    except IOError:
        print(f"Error: Unable to open file '{filename}'")

    labels = list(expenses.keys())
    values = list(expenses.values())
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, colors=colors)
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == '__main__':
    main()
