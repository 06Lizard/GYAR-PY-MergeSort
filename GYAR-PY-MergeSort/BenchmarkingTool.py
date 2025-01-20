from List import List
import keyboard
import time 
import random

class BenchmarkingTool:
    def __init__(self):
        self.list = List()

    def run(self):
        running = True
        while running:
            self.printMenu()
            choice = self.navigateMenu()

            if choice == 1:
                self.addRandomElements()
                time.sleep(0.5)
            elif choice == 2:
                self.addElement()
                time.sleep(0.5)
            elif choice == 3:
                self.removeElement()
                time.sleep(0.5)
            elif choice == 4:
                self.printElement()
                time.sleep(0.5)
            elif choice == 5:
                self.list.printAll()
                time.sleep(0.5)
            elif choice == 6:
                self.list.printFirst()
                time.sleep(0.5)
            elif choice == 7:
                self.list.printLast()
                time.sleep(0.5)
            elif choice == 8:
                self.list.boubbleSort()
                time.sleep(0.5)
            elif choice == 9:
                self.list.mergeSort()
                time.sleep(0.5)
            elif choice == 10:
                self.benchmarkSorts()
                time.sleep(0.5)
            elif choice == 11:
                running = False
                time.sleep(0.5)
            else:
                print("Invalid choice. Please try again.")
                time.sleep(0.5)

            print("\033[2J\033[1;1H")

    def navigateMenu(self):
        selectedIndex = 1
        print("\033[?25l"); # hide cursor

        while True:
            self.updateMenu(selectedIndex)
            if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
                selectedIndex = 1 if selectedIndex <= 1 else selectedIndex - 1
            elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
                selectedIndex = 11 if selectedIndex >= 11 else selectedIndex + 1
            elif keyboard.is_pressed('enter'):
                print("\033[?25h")
                return selectedIndex
            time.sleep(0.2)

    def printMenu(self):
        print("\033[2J\033[1;1H"
              "Menu:\n"
              "\t1. Add x random elements with value between y and z\n"
              "\t2. Add element\n"
              "\t3. Remove element\n"
              "\t4. Print element\n"
              "\t5. Print all elements\n"
              "\t6. Print first element\n"
              "\t7. Print last element\n"
              "\t8. Bubble sort\n"
              "\t9. Merge sort\n"
              "\t10. Benchmark bubble sort and merge sort (iterate x times with y elements each time)\n"
              "\t11. Exit")

    def updateMenu(self, selectedIndex):
        # Clear previous selections
        for i in range(1, 12):
            print("\033[{};1H   ".format(i+1))

        # Write selection arrow
        print("\033[{};1H>> ".format(selectedIndex + 1))

    def get_int_input(self, prompt):  # Add 'self' as the first argument
        while True:
            try:
                return int(input(prompt))  # Try to convert the input to an integer
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
    
    def get_float_input(self, prompt):  # Add 'self' as the first argument
        while True:
            try:
                return float(input(prompt))  # Try to convert the input to a float
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def addRandomElements(self):
        print("\033[2J\033[1;1HNote: Only whole numbers allowed!")
        num = self.get_int_input("Enter the number of elements to add: ")
        min_val = self.get_int_input("Enter the minimum value: ")
        max_val = self.get_int_input("Enter the maximum value: ")
        self.addRandomElements(num, min_val, max_val)

    def addRandomElements(self, num, min_val, max_val):
        for _ in range(num):
            random_value = random.randint(min_val, max_val)
            self.list.push(random_value)

    
    def addElement(self):
        value = self.get_float_input("\033[2J\033[1;1HEnter the value to add: ")
        self.list.push(value)
    
    def removeElement(self):
        index = self.get_int_input("\033[2J\033[1;1HEnter the index of the element to remove: ")
        self.list.removeElement(index)
    
    def printElement(self):
        index = self.get_int_input("\033[2J\033[1;1HEnter the index of the element to print: ")
        self.list.printElement(index)

    def benchmarkSorts(self):
        iterations = self.get_int_input("\033[2J\033[1;1HEnter the number of iterations: ")
        num_elements = int(input("Enter the number of elements for each iteration: "))

        merge_sort_times = []

        for i in range(iterations):
            print(f"Initializing list for iteration {i + 1}...")
            self.addRandomElements(num_elements, 0, 10000)

            print("Sorting with Merge Sort...")
            start = time.time()
            self.list.mergeSort()
            end = time.time()

            duration = (end - start) * 1000  # Convert to milliseconds
            print(f"Iteration {i + 1}: Merge Sort time = {duration:.3f} ms")
            merge_sort_times.append(duration)

            self.list.clear()

        # Calculate average merge sort time
        average_merge_sort_time = np.mean(merge_sort_times)
        print(f"\nAverage Merge Sort time: {average_merge_sort_time:.3f} ms")

        # Benchmark bubble sort (single iteration)
        print("\nRunning a singular Bubble Sort iteration...")
        self.addRandomElements(num_elements, 0, 10000)

        start = time.time()
        self.list.boubbleSort()
        end = time.time()

        bubble_sort_time = end - start
        print(f"Bubble Sort time: {bubble_sort_time:.3f} seconds")
        time.sleep(1)
        print("Press 'Enter' to continue.")
        while True:
            if keyboard.is_pressed('enter'):
                break
