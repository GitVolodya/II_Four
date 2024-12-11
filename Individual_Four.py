#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# С помощью алгоритма поиска с ограничением глубины найдем минимальное расстояние между начальным и конечным пунктами
import itertools

def calculate_total_distance(route, distance_matrix):
    """Вычисление общей дистанции для данного маршрута."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    # Добавляем расстояние обратно к начальной точке
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def traveling_salesman(distance_matrix):
    """Решение задачи коммивояжера методом полного перебора."""
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_route = None
    # Генерация всех возможных маршрутов
    for route in itertools.permutations(cities):
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
    return best_route, min_distance

# Пример использования
if __name__ == "__main__":  # Исправлено на __name__ == "__main__"
    # Матрица расстояний между городами для 10 узлов
    distance_matrix = [
        [0, 83, 224, 433, 549, 729, 886, 552, 441, 192],
        [83, 0, 150, 359, 475, 655, 812, 478, 367, 275],
        [224, 150, 0, 209, 325, 505, 662, 328, 217, 416],
        [433, 359, 209, 0, 116, 296, 453, 537, 426, 625],
        [549, 475, 325, 116, 0, 180, 337, 431, 542, 741],
        [729, 655, 505, 296, 180, 0, 157, 251, 362, 633],
        [886, 812, 662, 453, 337, 157, 0, 342, 453, 724],
        [552, 478, 328, 537, 431, 251, 342, 0, 111, 382],
        [441, 367, 217, 426, 542, 362, 453, 111, 0, 493],
        [192, 275, 416, 625, 741, 633, 724, 382, 493, 0],
    ]

    best_route, min_distance = traveling_salesman(distance_matrix)
    print(f"Лучший маршрут: {best_route}")
    print(f"Минимальное расстояние: {min_distance}")
