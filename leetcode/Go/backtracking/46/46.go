package main

// Created by chatgpt
func permute(nums []int) [][]int {
	var permutations [][]int
	var current []int // Permutación actual en construcción
	used := make([]bool, len(nums))
	var backtrack func()
	backtrack = func() {
		// Si la permutación tiene la longitud completa, agregarla al resultado
		if len(current) == len(nums) {
			// Hacer una copia de `current` porque se modifica en cada paso
			temp := make([]int, len(current))
			copy(temp, current)
			permutations = append(permutations, temp)
			return
		}

		// Explorar todas las opciones
		for i := 0; i < len(nums); i++ {
			if used[i] { // Si el número ya está en la permutación actual, saltarlo
				continue
			}

			// Incluir el número en la permutación actual
			current = append(current, nums[i])
			used[i] = true

			// Llamar recursivamente con el nuevo estado
			backtrack()

			// Retroceder: deshacer los cambios
			current = current[:len(current)-1]
			used[i] = false
		}
	}
	return permutations
}
