import heapq

def cheapest_path(t, start, finish):
    rows, cols = len(t), len(t[0])
    directions = [("down", 1, 0), ("up", -1, 0), ("right", 0, 1), ("left", 0, -1)]
    
    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    pq = [(0, start)]
    distances = {start: 0}
    predecessors = {start: None}

    while pq:
        current_cost, (current_r, current_c) = heapq.heappop(pq)

        if (current_r, current_c) == finish:
            path = []
            while (current_r, current_c) != start:
                prev_r, prev_c = predecessors[(current_r, current_c)]
                for direction, dr, dc in directions:
                    if (prev_r, prev_c) == (current_r - dr, current_c - dc):
                        path.append(direction)
                        break
                current_r, current_c = prev_r, prev_c
            return path[::-1]
        
        for direction, dr, dc in directions:
            next_r, next_c = current_r + dr, current_c + dc
            if in_bounds(next_r, next_c):
                next_cost = current_cost + t[next_r][next_c]
                if (next_r, next_c) not in distances or next_cost < distances[(next_r, next_c)]:
                    distances[(next_r, next_c)] = next_cost
                    predecessors[(next_r, next_c)] = (current_r, current_c)
                    heapq.heappush(pq, (next_cost, (next_r, next_c)))
    
    return []

"""
Автор: Дуплей Максим Игоревич
TG: @quadd4rv1n7
Дата: 21.12.2024
"""
