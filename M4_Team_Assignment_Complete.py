#Module 4: Team Assignment



print("You just woke up, how are you going to start your day?") 
print("1. Make your bed")
print("2. Brush your teeth")
print("3. Clean your room")
print("4. Do push ups")
print("5. Stretch")
print("6. Make breakfast")
print("7. Shower")
print("8. Get dressed")
print("0. Exit")
variable_name = int(input())
match variable_name:
    case 1:
        print("You made your bed quicky.")
    case 2:
        print("You brushed your pearly whites.")
    case 3:
        print("You cleaned up, nice and tidy.")
    case 4:
        print("You feel stronger.")
    case 5:
        print("I feel so relaxed after I streached.")
    case 6:
        print("You made naan and eggs for breakfast.")
    case 7:
        print("You feel clean and refreshed.")
    case 8:
        print("I like the way you dress up so religiously.")
    case 0:
        print("Where are we going?")