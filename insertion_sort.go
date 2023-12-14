package main

import "fmt"

func insertionSort(slice []int) []int {
	// итерируемся по срезу, начиная со второго элемента
	for i := 1; i < len(slice); i++ {
		// сохраняем текущий элемент
		current := slice[i]
		// итерируемся по отсортированной части среза справа налево
		j := i - 1
		for j >= 0 && slice[j] > current {
			// сдвигаем элементы вправо
			slice[j+1] = slice[j]
			j--
		}
		// вставляем текущий элемент в правильную позицию в отсортированной части среза
		slice[j+1] = current
	}
	return slice
}

func main() {
	// создаём неотсортированный срез целых чисел
	s := []int{5, 2, 4, 6, 1, 3}

	// печатаем неотсортированный срез
	fmt.Println("Неотсортированный:", s)

	// сортируем срез с помощью сортировки вставками
	sorted := insertionSort(s)

	// печатаем отсортированный срез
	fmt.Println("Отсортированный:", sorted)
}
