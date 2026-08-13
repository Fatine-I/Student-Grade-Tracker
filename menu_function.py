def main():
    tracker=GradeTracker()
    while True:
        print("GRADE TRACKER\n\n\n")
        print("1. Add homework")
        print("2. Add exam")
        print("3. List assignments")
        print("4.Filter assignments")
        print("5. Show summary")
        print("6. Exit")
    choice=input("\nChoose an option: ").strip()
    if choice=="1":
        choice2=input("1. Add homework\n2.Press Enter to return to the main menu").strip()
        while choice2=="1":
            tracker.add_homework()
        else: 
            input("\nPress Enter to return to the main menu")
    elif choice == "2":
        choice2=input("1. Add homework\n2.Press Enter to return to the main menu").strip()
        while choice2=="1":
            tracker.add_exam()
        else:
            input("\nPress Enter to return to the main menu")

    elif choice=="3":
        tracker.list_assignment()
        input("\nPress Enter to return to the main menu")
    elif choice=="4":
        tracker.filter_assignment()
        input("\nPress Enter to return to the main menu")
    elif choice=="5":
        tracker.summary()
        input("\nPress Enter to return to the main menu")
    elif choice=="6":
        exit()
    else:
        print("\nInvalid choice. Please choose 1-6")
        input("\nPress Enter to return to the main menu")