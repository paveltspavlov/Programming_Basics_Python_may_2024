facebook_tab = 150
instagram_tab = 100
reddit_tab = 50

number_of_opened_tabs = int(input())
salary = int(input())

facebook_fine = 0
instagram_fine = 0
reddit_fine = 0
total_fine = 0

for i in range(number_of_opened_tabs):
    tab = input()
    if tab == "Facebook":
        facebook_fine += 1
        i += i
    elif tab == "Instagram":
        instagram_fine += 1
        i += i
    elif tab == "Reddit":
        reddit_fine += 1
        i += i
    else:
        i += i
    total_fine = facebook_fine * facebook_tab + instagram_fine * instagram_tab + reddit_fine * reddit_tab
    if total_fine >= salary:
        print(f"You have lost your salary.")
        break

if total_fine < salary:
    diff = salary - total_fine
    print(diff)
