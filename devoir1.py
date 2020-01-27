#Tentative 1

# f1 = "https://montrealcampus.ca/?p="
# f2 = list(range(20000, 30150))
# f3 = f1+f2
# print(f3)

#TENTATIVE 2
# f1 = "https://montrealcampus.ca/?p="
# f2 = str(list(range(20000, 30151)))
# f3 = f1+f2
# print(f3)

#TENTATIVE 3
# f1 = str(list(range(20000, 30151)))
# print(f1)

# n = 0
# for list in f1:
#     n += 1
#     print(f1)


#TENTATIVE 4
# f1 = ["https://montrealcampus.ca/?p=20000", "https://montrealcampus.ca/?p=20001", "https://montrealcampus.ca/?p=20002", "https://montrealcampus.ca/?p=20003"]
# f1.append("https://montrealcampus.ca/?p=" + str(list(range(20000, 30151))))
# print(f1)

#TENTATIVE 5
f1 = list(range(20000, 30151))

n = 0
for articles in f1:
    n += 1
    print(n)
    print("https://montrealcampus.ca/?p=" + str(articles))
