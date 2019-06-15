import random

class node :
    def __init__(self, name = None) :
        self.name = name
        self.neighbours = {}

class graph :
    def __init__(self, adj_arr) :
        self.node_list = []
        for i in range(len(adj_arr)) :
            newnode = node(i+1)
            self.node_list.append(newnode)
        for i in range(len(self.node_list)) :
            for j in range(len(self.node_list)) :
                if adj_arr[i][j] != '-' :
                    self.node_list[i].neighbours[self.node_list[j]] = adj_arr[i][j]

    def get_all_nodes(self) :
        return self.node_list


def read_text_file(file_add) :
    txtfile = open(file_add, 'r')
    lines = txtfile.read().split('\n')
    for i in range(len(lines)) :
        lines[i] = lines[i].split(',')
        for ind in range(len(lines[i])) :
            if lines[i][ind] != '-' :
                lines[i][ind] = int(lines[i][ind])
    txtfile.close()
    return lines


def pathfinder(graph_struct) :
    all_nodes = graph_struct.get_all_nodes()
    pathsum = 0
    uncon_nodes = all_nodes.copy()
    wt_dict = {}
    curr_node = random.choice(uncon_nodes)

    def visit_curr_node(curr_node) :
        for nbr in curr_node.neighbours.keys() :
            if curr_node.neighbours[nbr] in wt_dict.keys() :
                wt_dict[curr_node.neighbours[nbr]].append(nbr)
            else : wt_dict[curr_node.neighbours[nbr]] = [nbr]
        uncon_nodes.remove(curr_node)

    def clean_dict(wt_dict) :
        empty_keys = []
        for k in wt_dict.keys() :
            for node_pt in wt_dict[k] :
                if node_pt not in uncon_nodes :
                    wt_dict[k].remove(node_pt)
            if len(wt_dict[k]) == 0 :
                empty_keys.append(k)
        for val in empty_keys : wt_dict.pop(val)

    visit_curr_node(curr_node)

    while len(uncon_nodes) > 0 :
        min_wt = min(wt_dict.keys())
        curr_node = random.choice(wt_dict[min_wt])
        pathsum += min_wt
        visit_curr_node(curr_node)
        wt_dict[min_wt].remove(curr_node)
        if len(wt_dict[min_wt]) == 0: wt_dict.pop(min_wt)

        clean_dict(wt_dict)

    return pathsum

arr_adj = read_text_file('p107_network.txt')
run_graph = graph(arr_adj)
shortsum = pathfinder(run_graph)

print('Gain : ', sum([val for l1 in arr_adj for val in l1 if val != '-'])/2 - shortsum)