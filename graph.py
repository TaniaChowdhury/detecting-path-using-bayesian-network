link = 'links.txt'

pos = 'pos.txt'

# name of output file
tab = 'table.txt'
tab = open(tab, 'w')

paths = []
# read text files
with open(link) as file:
    while (line := file.readline().rstrip()):
        line = line.split(' ')
        ln = []
        for i in line:
            ln.append(int(i))
        # paths is a 2-D list that show connection between nodes
            """ each (1) show a link  """
        paths.append(ln)


two_link = []

node_num = len(paths)


# this function examine each node and find path  input or output are head or tain
def get_link(g, i):

    num = len(g)
    lns = []
    # loop for all nodes come in or out to current node
    for j in range(num):
        if g[j][i] == 1 and i != j:
            lns.append([j, 'H'])
        if g[i][j] == 1 and i != j:
            lns.append([j, 'T'])

    out = []
    l2 = len(lns)
    idx = []
    # loops for all states may be a path
    for j1 in range(l2-1):
        for j2 in range(j1+1, l2):
            if lns[j1][0] != lns[j2][0]:
                label = lns[j1][1]+lns[j2][1]
                lnk = 'X'+str(lns[j1][0]+1)+'X'+str(i+1)+'X'+str(lns[j2][0]+1)
                out.append([label, lnk])
    return out


tbl = []

for i in range(node_num):
    # loop for all nodes and call above function to find each path
    node_two = get_link(paths, i)
    tbl.append(node_two)


all_p = []
node = 0
# making unique pahtes,may  be some reapitive values existance
for a in tbl:
    node = node+1
    for b in a:
        ch = True

        for z in range(len(all_p)):
            if all_p[z][0][1] == b[1]:
                ch = False

        if ch == True:
            all_p.append([b, node])

# write output of pathsto text file name table.tx in first
for item in all_p:
    tab.write(' p'+str(item[1])+'        '+item[0][0]+'        '+item[0][1])
    tab.write('\n')


tab.close()


xy = []
# getting cordinate of yoour graph if you wana to plot
with open(pos) as file:
    while (line := file.readline().rstrip()):
        line = line.split(' ')
        ln = []
        for i in line:
            ln.append(float(i))
        xy.append(ln)


try:
    import matplotlib.pyplot as plt

    siz = len(paths)
    # loop for find links and plot theme
    for i in range(siz):
        for j in range(siz):
            if paths[i][j] == 1:
                x = [xy[i][1], xy[j][1]]
                y = [xy[i][2], xy[j][2]]
                plt.plot(x, y)

    # loop for plot name of nodes
    for i in range(siz):
        plt.text(xy[i][1], xy[i][2], 'X'+str(i))

    plt.title('showing graph')
    plt.savefig('image')
    plt.show()


except:
    print('please install matplotlib')
