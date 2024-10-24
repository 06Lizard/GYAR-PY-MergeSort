# initiazised
#from List import a
import List

# main function
if __name__ == "__main__":
    myList = List.List()
    myList.push(5)
    myList.push(4)
    myList.push(3)
    myList.push(2)
    myList.push(1)
    myList.boubbleSort()
    myList.printAll()
    print(myList.getSize())


# any other function