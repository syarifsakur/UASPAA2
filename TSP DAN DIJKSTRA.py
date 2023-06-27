#Nama  : Syarif Mohammad Syakur
#NIM   : F55121020
#Kelas : A

import time
import sys

def tsp(graph, start):
    num_nodes = len(graph)
    visited = {node: False for node in graph}
    visited[start] = True
    path = [start]
    total_distance = 0
    curr_node = start

    while len(path) < num_nodes:
        min_distance = sys.maxsize
        next_node = None

        for node in graph[curr_node]:
            if not visited[node] and graph[curr_node][node] < min_distance:
                next_node = node
                min_distance = graph[curr_node][node]

        if next_node is None:
            break

        path.append(next_node)
        visited[next_node] = True
        total_distance += min_distance
        curr_node = next_node
        print(f"Iterasi {len(path) - 1}: Path = {path}, Distance = {total_distance}")

    path.append(start)
    total_distance += graph[curr_node][start]
    print(f"Hasil Akhir: Path = {path}, Distance = {total_distance}")
    return path, total_distance

def dijkstra(graph, start):
    num_nodes = len(graph)
    distance = {node: sys.maxsize for node in graph}
    distance[start] = 0
    visited = {node: False for node in graph}
    path = [start]
    curr_node = start

    while len(path) < num_nodes:
        min_distance = sys.maxsize
        next_node = None

        for node in graph[curr_node]:
            if not visited[node] and graph[curr_node][node] < min_distance:
                next_node = node
                min_distance = graph[curr_node][node]

        if next_node is None:
            break

        path.append(next_node)
        visited[next_node] = True
        distance[next_node] = distance[curr_node] + min_distance
        curr_node = next_node
        print(f"Iterasi {len(path) - 1}: Path = {path}, Distance = {distance[next_node]}")

    print(f"Hasil Akhir: Path = {path}, Distance = {distance[curr_node]}")
    return path, distance[curr_node]

def main():

    graph = {
        'a': {'b': 12, 'c': 10, 'g': 12},
        'b': {'a': 12, 'c': 8, 'd': 12},
        'c': {'b': 8, 'a': 10, 'd': 11, 'e': 3},
        'd': {'b': 12, 'c': 11, 'e': 11},
        'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
        'f': {'e': 6, 'g': 9},
        'g': {'a': 12, 'e': 7, 'f': 9}
    }

    print("Grafik:")
    for node in graph:
        print(node, end=' ')
    print()

    print("Pilihlah algoritma yang ingin digunakan :")
    print("1.TSP")
    print("2.DIJSKTRA")
    algorithm = input("Pilih:")

    if algorithm == "1":
        start = input("Masukkan node awal: ").lower()
        start_time = time.time()
        shortest_path, total_distance = tsp(graph, start)
        end_time = time.time()
        print(f"Waktu komputasi: {end_time - start_time} detik")

    elif algorithm == "2":
        start = input("Masukkan node awal: ").lower()
        start_time = time.time()
        shortest_path, total_distance = dijkstra(graph, start)
        end_time = time.time()
        print(f"Waktu komputasi: {end_time - start_time} detik")

    else:
        print("Algoritma yang dimasukkan tidak valid. Program berakhir.")

if __name__ == '__main__':
    main()