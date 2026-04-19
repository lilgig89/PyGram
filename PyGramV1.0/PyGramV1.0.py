#Copyright (c) 2026 Lilgigggg
import os
import webbrowser

scelta = -1
uno = False
while scelta != 0:
    print("1 - Entering names")
    print("2 - Name Search (First Group)")
    print("3 - Name Search (Second Group)")
    print("0 - Exit")

    scelta = int(input("Choice: "))

    match scelta:
        case 1:
            uno = True
            listanomi = []
            listanomi1 = []

            n = input("Name: ").strip().lower()
            c = input("Surname: ").strip().lower()

            listanomi.append(f"_{n}.{c}_")
            listanomi.append(f"{n}.{c}")
            listanomi.append(f"{n}{c}")
            listanomi.append(f"{n}_{c}")
            listanomi.append(f"{n}_{c}_")
            listanomi.append(f"{n}{c}_")
            listanomi.append(f"_{c}.{n}_")
            listanomi.append(f"{c}.{n}")
            listanomi.append(f"{c}{n}")
            listanomi.append(f"{c}_{n}")
            listanomi.append(f"{c}_{n}_")
            listanomi.append(f"{c}{n}_")
            listanomi1.append(f"_{n}.{c}_1")
            listanomi1.append(f"{n}.{c}1")
            listanomi1.append(f"{n}{c}1")
            listanomi1.append(f"{n}_{c}1")
            listanomi1.append(f"{n}_{c}_1")
            listanomi1.append(f"{n}{c}_1")
            listanomi1.append(f"_{c}.{n}_1")
            listanomi1.append(f"{c}.{n}1")
            listanomi1.append(f"{c}{n}1")
            listanomi1.append(f"{c}_{n}1")
            listanomi1.append(f"{c}_{n}_1")
            listanomi1.append(f"{c}{n}_1")
        case 2:
            if(uno == True):
                for i in range(len(listanomi)):
                    print(listanomi[i])
                    webbrowser.open_new_tab(f"https://www.instagram.com/{listanomi[i]}")
            else:
                print("Enter names first")
        case 3:
            if(uno == True):
                for i in range(len(listanomi1)):
                    print(listanomi1[i])
                    webbrowser.open_new_tab(f"https://www.instagram.com/{listanomi1[i]}")
            else:
                print("Enter names first")
        case 0:
            print("Exit")