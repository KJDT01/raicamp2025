#txt="rai" #เก็บตัวแปรชั่วคราว ทุกครั้งที่เปิดโปรแกรมใหม่ข้อมูลจะหาย
#print(txt)
#fruit = "apple" #เก็บตัวเดียว


#fruits = ["apple", "banana"] #เก็บหลายตัว
#fruits.append ("orange") #แทรกเข้ามา แต่ได้ตัวเดียว ต่อหลัง
#fruits.remove("apple")
#fruits.insert(0,"melon") #ตำแหน่งที่แทรก แทรก
#for fruit in fruits:
#    print(f"This is a {fruit}.")


#i=0
#while i<3:
#    print(i) #ช่องด้านหน้าว่าง4ช่อง
#    i=i+1
#print("done")


#### Dictionary in Mobile Robot
#            A
#           / \
#          B   C
#         / \   \
#        D   E   F

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[],
}

start = 'A'
goal ='C'
frontier = [start]
explored = set() # จะไม่เบิ้ลข้อมูลเป็น2ชุด

print(frontier, explored)

while len(frontier)>0:
    current = frontier.pop() # Remove and put into varaible
    print(current)

    if current == goal:
        print("Goal reach")
        break
    
    for neighbor in graph[current]:
        frontier.append(neighbor)    

