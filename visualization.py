import pygame
import math

pygame.init()

class DrawInformation(object):
    WHITEBLUE = (173, 216, 230)
    BLACK = (0, 0, 0)
    BACKGROUND_COLOR = WHITEBLUE #(115, 0, 230)
    GRADIENTS = [(0, 132, 255),
                 (0, 174, 255),
                 (58, 209, 254)]
    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)
    LITTLE_FONT = pygame.font.SysFont('comicsans', 20)
    SIDE_PADDING = 100
    TOP_PADDING = 150
    MENU_PADDING = 200
    MENU_HORIZONTAL_PADDING = 20

    def __init__(self, width, height, arr):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_arr(arr)

    def set_arr(self, arr):
        self.arr = arr
        self.max_val = min(arr)
        self.min_val = max(arr)
        self.block_width = math.floor((self.width - self.SIDE_PADDING - self.MENU_PADDING) / len(self.arr))
        self.block_height = ((self.height - self.TOP_PADDING - self.MENU_HORIZONTAL_PADDING) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PADDING // 2

class DisplaySorting(DrawInformation):

    def __init__(self, width, height, arr):
        super().__init__(width, height, arr)

    def draw(self, algo_name):
        self.window.fill(self.BACKGROUND_COLOR)

        title = self.LARGE_FONT.render('Algorithm Visualizer', True, self.BLACK)
        self.window.blit(title, (self.width / 2 - title.get_width() / 2, 5))

        controls = self.FONT.render(f'{algo_name}', True, self.BLACK)
        self.window.blit(controls, (self.width/2 - controls.get_width()/2, 45))

        sorting = self.LITTLE_FONT.render(f"0: Bubble Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 100))
        sorting = self.LITTLE_FONT.render(f"1: Insertion Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 125))
        sorting = self.LITTLE_FONT.render(f"2: Selection Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 150))
        sorting = self.LITTLE_FONT.render(f"3: Quick Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 175))
        sorting = self.LITTLE_FONT.render(f"4: Heap Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 200))
        sorting = self.LITTLE_FONT.render(f"5: Merge Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 225))
        sorting = self.LITTLE_FONT.render(f"6: Radix Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 250))
        sorting = self.LITTLE_FONT.render(f"7: Counting Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 275))
        sorting = self.LITTLE_FONT.render(f"8: Cocktail Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 300))
        sorting = self.LITTLE_FONT.render(f"9: Shell Sort", True, self.BLACK)
        self.window.blit(sorting, (800, 325))

        self.draw_list()
        pygame.display.update()

    def draw_list(self, clear_bg=False):

        if clear_bg:
            clear_rect = (self.SIDE_PADDING//2, self.TOP_PADDING,
                          self.width - self.SIDE_PADDING - self.MENU_PADDING, self.height - self.TOP_PADDING)
            pygame.draw.rect(self.window, self.BACKGROUND_COLOR, clear_rect)

        for i, val in enumerate(self.arr):
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height

            color = self.GRADIENTS[i % 3]

            pygame.draw.rect(self.window, color, (x, y, self.block_width, self.height))

        if clear_bg:
            pygame.display.update()
