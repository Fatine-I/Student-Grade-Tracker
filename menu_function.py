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
            tracker.add_homework() 
            input("\nPress Enter to return to the main menu")
        elif choice == "2":
            tracker.add_exam()
            input("\nPress Enter to return to the main menu")
        elif choice=="3":
            tracker.list_assignments()
            input("\nPress Enter to return to the main menu")
        elif choice=="4":
            tracker.filter_assignments()
            input("\nPress Enter to return to the main menu")
        elif choice=="5":
            tracker.summary()
            input("\nPress Enter to return to the main menu")
        elif choice=="6":
            break
        else:
            print("\nInvalid choice. Please choose 1-6")
            input("\nPress Enter to return to the main menu")

if __name__=="__main__": 
    main()