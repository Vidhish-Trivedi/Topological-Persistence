FILE_PATH = "./tests/GNUTieFighter.txt"
v = 0
e = 0
f = 0

cnt = 0
new_list = []
vertices = []
edges = []
faces = []
print(f"Reading from {FILE_PATH}...\n")
with open(FILE_PATH) as file:
    for line in file:
        line = line.rstrip().split()
        if(cnt == 0):
            v = line[0]
            e = line[1]
            f = line[2]
            vertices = [i for i in range(1, int(v) + 1)]
        if(cnt > int(v) and cnt <= int(v) + int(e)):
            # print(edges)
            # add edges
            edges.append((line[0], line[1]))
        if(cnt > int(v) + int(e)):
            s = set([edges[int(line[0]) - 1][0], edges[int(line[0]) - 1][1], edges[int(line[1]) - 1][0],
                    edges[int(line[1]) - 1][1], edges[int(line[2]) - 1][0], edges[int(line[2]) - 1][1]])
            faces.append(list(s))
        cnt += 1


print(f"Writing to {FILE_PATH.replace('.txt','_out.txt')}...\n")
t = 0.0
with open(FILE_PATH.replace('.txt', '_out.txt'), 'w') as file:
    for i in range(0, len(vertices)):
        file.write(f"{t} 0 {vertices[i]}\n")
        t += 1
with open(FILE_PATH.replace('.txt', '_out.txt'), 'a') as file:
    for i in range(0, len(edges)):
        file.write(str(t) + " 1 " + str(edges[i][0]) + " " + str(edges[i][1]) + "\n")
        t += 1
with open(FILE_PATH.replace('.txt', '_out.txt'), 'a') as file:
    for i in range(0, len(faces)):
        file.write(f"{t} 2 {faces[i][0]} {faces[i][1]} {faces[i][2]}\n")
        t += 1
