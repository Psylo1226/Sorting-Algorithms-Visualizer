import pygame
from visualization import DisplaySorting
import algorithms
import random


def main():
    run = True
    clock = pygame.time.Clock()

    n = 75
    min_val = 0
    max_val = 500

    arr = random.sample(range(min_val, max_val), n)
    draw_info = DisplaySorting(1000, 600, arr)
    sorting = False

    sorting_algorithm = algorithms.bubble_sort
    sorting_algo_name = 'Bubble Sort'
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw_info.draw(sorting_algo_name)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                arr = random.sample(range(min_val, max_val), n)
                draw_info.set_arr(arr)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info)
            elif event.key == pygame.K_0 and not sorting:
                sorting_algorithm = algorithms.bubble_sort
                sorting_algo_name = 'Bubble Sort'
            elif event.key == pygame.K_1 and not sorting:
                sorting_algorithm = algorithms.insertion_sort
                sorting_algo_name = 'Insertion Sort'
            elif event.key == pygame.K_2 and not sorting:
                sorting_algorithm = algorithms.selection_sort
                sorting_algo_name = 'Selection Sort'
            elif event.key == pygame.K_3 and not sorting:
                sorting_algorithm = algorithms.quick_sort
                sorting_algo_name = 'Quick Sort'
            elif event.key == pygame.K_4 and not sorting:
                sorting_algorithm = algorithms.heap_sort
                sorting_algo_name = 'Heap Sort'
            elif event.key == pygame.K_5 and not sorting:
                sorting_algorithm = algorithms.merge_sort
                sorting_algo_name = 'Merge Sort'
            elif event.key == pygame.K_6 and not sorting:
                sorting_algorithm = algorithms.radix_sort
                sorting_algo_name = 'Radix Sort'
            elif event.key == pygame.K_7 and not sorting:
                sorting_algorithm = algorithms.counting_sort2
                sorting_algo_name = 'Counting Sort'
            elif event.key == pygame.K_8 and not sorting:
                sorting_algorithm = algorithms.cocktail_sort
                sorting_algo_name = 'Cocktail Sort'
            elif event.key == pygame.K_9 and not sorting:
                sorting_algorithm = algorithms.shell_sort
                sorting_algo_name = 'Shell Sort'

    pygame.quit()

if __name__ == '__main__':
    main()
