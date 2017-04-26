# -*- coding: utf-8 -*-
# Python 3.6.1

import os

PYLIB_DIR = "./pylib/"
dependency = {}

filenames = os.listdir(PYLIB_DIR)
for filename in filenames:
    if filename.endswith(".py"):
        dependency[filename[:-3]] = []

custom_modules = list(dependency.keys())

for filename in filenames:
    if filename.endswith(".py"):
        file = open(PYLIB_DIR + filename, "r")
        for line in file:
            l = line.split()
            if len(l) == 2 and l[0] == "import" and l[1] in custom_modules:
                dependency[filename[:-3]].append(l[1])
        file.close()

dep_graph = open("dependency_graph.txt", "w")
custom_modules.sort()
dep_graph.write("This file gives the list of modules and its importing modules.\n")
dep_graph.write("The list is sorted alphabetically.\n")
for module in custom_modules:
    if dependency[module] == []:
        dep_graph.write(" - " + module + ": None\n")
    else:
        dep_graph.write(" - " + module + ": " + ", ".join(dependency[module]) + "\n")
dep_graph.close()



def acc_graph(graph_dic):
    result = {}
    for v in graph_dic.keys():
        reachable = []
        next_search = [v]
        while next_search != []:
            w = next_search.pop(0)
            if w not in reachable:
                reachable.append(w)
                for u in graph_dic[w]:
                    next_search.append(u)
        reachable.remove(v)
        result[v] = reachable
    return result

acc_dependency = acc_graph(dependency)

acc_graph = open("full_dependency.txt", "w")
acc_graph.write("This file gives the list of modules and its necessary modules.\n")
acc_graph.write("Necessary modules are modules that are needed to run specific module.\n")
acc_graph.write("For example, if module A imports module B and module B imports module C,\n")
acc_graph.write("then to run module A, module B and C both are needed.\n")
acc_graph.write("The list is sorted alphabetically.\n")
for module in sorted(acc_dependency.keys()):
    if acc_dependency[module] == []:
        acc_graph.write(" - " + module + ": None\n")
    else:
        acc_graph.write(" - " + module + ": " + ", ".join(acc_dependency[module]) + "\n")
acc_graph.close()



# TODO: Add module bundler here
#   Input: module name
#   Output: bundled module file(get all necessary modules in one file)
#           in current directory
