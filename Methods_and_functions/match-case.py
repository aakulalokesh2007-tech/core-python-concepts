
match input("Enter yes or no: ").strip().lower():
    case "yes" | "y": # You can even use the '|' operator to allow multiple options!
        print("ok")
    case "no" | "n":
        print("byee")
    case _:
        print("else")