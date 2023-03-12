<p align="center">
  <img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/Sorting_Algorithms_Visualizer.png" width="700" height="350">
</p>
<h1 align="center">Sorting-Algorithms-Visualizer</h1>




- [1. Algorithms Preview](#1-algorithms-preview)
- [2. Installation](#2-installation)
- [3. Get Started](#3-get-started)

## 1. Algorithms Preview

<div>
<h2>Bubble Sort</h2>

Bubble sort is a simple sorting algorithm that repeatedly steps through a list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. It's called "bubble" sort because the smaller elements "bubble" to the top of the list with each iteration. Bubble sort has a worst-case and average-case time complexity of O(n^2), making it inefficient for large lists, and is generally only used for educational purposes or for small, nearly-sorted lists.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/bubble_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $n$<br>
    Avg time complexity: $n^{2}$<br>
    Worst time complexity: $n^{2}$<br>
  </p>
</div>

<div>  
<h2>Insertion Sort</h2>

Insertion sort is a simple sorting algorithm that iterates through an array, comparing each element with the previous elements and swapping them until they are in the correct order. It starts by considering the first element as a sorted subarray and then iteratively builds up the sorted subarray by inserting each subsequent element into its correct position. Insertion sort has an average-case time complexity of O(n^2), but is efficient for small arrays or partially sorted arrays, and has a best-case time complexity of O(n) for already sorted arrays.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/insertion_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $n$<br>
    Average time complexity: $n^{2}$<br>
    Worst time complexity: $n^{2}$<br>
  </p>
 </div>
 
<div>
<h2>Selection Sort</h2>
  
Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from an unsorted part of the array and places it at the beginning of the array until the entire array is sorted. It has a worst-case and average-case time complexity of O(n^2), making it inefficient for large arrays, but is simple to implement and has an advantage over other algorithms in terms of the number of swaps performed, which can be important in some cases.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/selection_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $n^{2}$<br>
    Average time complexity: $n^{2}$<br>
    Worst time complexity: $n^{2}$<br>
  </p>
</div>
 
<div>
<h2>Quick Sort</h2>

Quick sort is a divide-and-conquer sorting algorithm that works by partitioning an array into two subarrays, then recursively sorting each subarray. It works by selecting a pivot element, then partitioning the array into two subarrays: one with elements less than the pivot and one with elements greater than the pivot. This pivot selection and partitioning process is repeated on each subarray until the entire array is sorted. Quick sort has an average-case time complexity of O(n log n) and a worst-case time complexity of O(n^2), but is often faster than other sorting algorithms in practice due to its efficient partitioning and cache usage.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/quick_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $nlogn$<br>
    Average time complexity: $nlogn$<br>
    Worst time complexity: $n^{2}$<br>
  </p>
</div>
 
<div>
<h2>Heap Sort</h2>

Heap sort is a comparison-based sorting algorithm that works by first building a max-heap from the input array, then repeatedly extracting the maximum element from the heap and placing it at the end of the array until the entire array is sorted. The max-heap is built by rearranging the array elements into a binary heap structure, where each parent node is greater than or equal to its child nodes. Heap sort has a worst-case and average-case time complexity of O(n log n), making it an efficient sorting algorithm for large arrays.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/heap_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $nlogn$<br>
    Average time complexity: $nlogn$<br>
    Worst time complexity: $nlogn$<br>
  </p>
</div>

<div>
<h2>Merge Sort</h2>

Merge sort is a divide-and-conquer sorting algorithm that works by dividing the input array into two halves, recursively sorting each half, and then merging the sorted halves back together. The merge step involves comparing the elements of the two sorted subarrays and placing them in the correct order in a temporary array, which is then copied back to the original array. Merge sort has an average-case and worst-case time complexity of O(n log n), making it an efficient sorting algorithm for large arrays, but requires additional memory for the temporary array used in the merge step.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/merge_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $nlogn$<br>
    Average time complexity: $nlogn$<br>
    Worst time complexity: $nlogn$<br>
  </p>
</div>
  
<div>
<h2>Radix Sort</h2>

Radix sort is a non-comparison-based sorting algorithm that works by sorting elements by their digit values, from least significant digit to most significant digit. It iterates through each digit position and sorts the elements into buckets based on that digit, then concatenates the buckets in order to obtain a sorted array. Radix sort can be implemented with either a least significant digit (LSD) or most significant digit (MSD) approach, and has a time complexity of O(d*(n+k)), where d is the number of digits, n is the number of elements, and k is the range of digit values. Radix sort is often used for sorting large integers, but requires the input elements to have a fixed size and a well-defined radix (i.e., base).<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/radix_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $n$<br>
    Average time complexity: $n\frac{k}{d}$<br>
    Worst time complexity: $n\frac{k}{d}$<br>
  </p>
</div>
  
<div>
<h2>Counting Sort</h2>

Counting sort is a non-comparison-based sorting algorithm that works by determining the frequency of each element in the input array, then using this frequency information to place each element in its correct position in a sorted output array. It works by iterating through the input array and counting the number of times each element appears, then using this information to determine the position of each element in the output array. Counting sort has a time complexity of O(n+k), where n is the number of elements and k is the range of input values, making it an efficient algorithm for sorting arrays with a small range of values. However, counting sort requires additional memory proportional to the range of values and is not suitable for sorting arrays with large or unbounded ranges.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/counting_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $O(n+k)$<br>
    Average time complexity: $O(n+k)$<br>
    Worst time complexity: $O(n+k)$<br>
  </p>
</div>
  
<div>
<h2>Cocktail Sort</h2>

Cocktail sort, also known as bidirectional bubble sort or shaker sort, is a variation of the bubble sort algorithm that works by repeatedly iterating through the array in both directions, comparing adjacent elements and swapping them if they are in the wrong order. In each pass, the largest element is bubbled to the top of the array and the smallest element is bubbled to the bottom, alternating between the left-to-right and right-to-left directions. Cocktail sort has a worst-case and average-case time complexity of O(n^2), the same as bubble sort, but can perform better in some cases due to the bidirectional approach. However, cocktail sort still suffers from the inefficiency of bubble sort and is generally only used for educational purposes or small, nearly-sorted arrays.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/cocktail_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $n$<br>
    Average time complexity: $n^{2}$<br>
    Worst time complexity: $n^{2}$<br>
  </p>
</div>  

<div>
<h2>Shell Sort</h2>

Shell sort is an efficient variation of the insertion sort algorithm that works by sorting elements at a certain distance apart, then gradually reducing this distance until the entire array is sorted. It works by dividing the input array into smaller subarrays, each of which is sorted using an insertion sort algorithm with a fixed gap between elements. The gap is then reduced, and the process is repeated on the smaller subarrays until the gap is 1, at which point a final insertion sort is performed. Shell sort has a worst-case and average-case time complexity of O(n log n), making it more efficient than simple sorting algorithms like bubble sort and insertion sort, but less efficient than more advanced algorithms like merge sort and quick sort.<br>
  <br>
<img src="https://github.com/Psylo1226/Sorting-Algorithms-Visualizer/blob/main/pictures/shell_sort_gif.gif" width="500" height="300"> <br>
  <p>
    Best time complexity: $nlogn$<br>
    Average time complexity: $n^{4/3}$<br>
    Worst time complexity: $n^{3/2}$<br>
  </p>
</div>

## 2. Installation

```bash
git clone https://github.com/<YOUR-USERNAME>/Sorting-Algorithms-Visualizer
```

Install requirements use:

```bash
cd Sorting-Algorithms-Visualizer
pip install -r requirements.txt
```

Runn App:

```bash
cd Sorting-Algorithms-Visualizer
python3 main.py
```

## 3. Get Started

Running **_main.py** you can start sorting array (in descending order) represented by bars.

- Select sorting algorithm by pressing:

<kbd>0</kbd> : Bubble Sort
     
<kbd>1</kbd> : Insertion Sort
     
<kbd>2</kbd> : Selection Sort
     
<kbd>3</kbd> : Qucik Sort
     
<kbd>4</kbd> : Heap Sort
     
<kbd>5</kbd> : Merge Sort
     
<kbd>6</kbd> : Radix Sort
     
<kbd>7</kbd> : Counting Sort
     
<kbd>8</kbd> : Cocktail Sort

<kbd>9</kbd> : Shell Sort

- Press <kbd>Space</kbd> to start sorting

- To shuffle and create new array hit <kbd>R</kbd>
