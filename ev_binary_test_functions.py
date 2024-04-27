# -*- coding: utf-8 -*-
"""EV Binary test functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uc7FHsBRKXP2fEfy24uNPdORkeM7awzO
"""

# Implement 5 arbitrary objective functions for testing that take binary string of a specified length (problem dimension) as an input.
# Examples:
# - Leading ones/zeros
# - OneMax
# - Decadic value of the bit string
# - Longest 1 chain
# - Switching sequence - 101010101010
# - etc.

# install needed libraries
import numpy as np

# define the binary string length as per desired length
binary_string_length = 16

# define the binary string
binary_string = np.random.randint(2, size=binary_string_length)

# 1. OneMax
def onemax(binary_string):
    return np.sum(binary_string)

# 2. Longest 1 Chain
def longest_1_chain(binary_string):
    max_chain_length = 0
    current_chain_length = 0
    for bit in binary_string:
        if bit == 1:
            current_chain_length += 1
            max_chain_length = max(max_chain_length, current_chain_length)
        else:
            current_chain_length = 0
    return max_chain_length

# 3. Royal Road
def royal_road(binary_string):
    block_size = 4  # Define the block size for the Royal Road function
    fitness = 0
    for i in range(0, binary_string_length, block_size):
        block = binary_string[i:i+block_size]
        if np.all(block == 1):
            fitness += block_size
    return fitness

# 4. Deceptive Trap
def deceptive_trap(binary_string):
    trap_size = 4  # Define the trap size for the Deceptive Trap function
    fitness = 0
    for i in range(0, binary_string_length, trap_size):
        trap = binary_string[i:i+trap_size]
        ones_count = np.sum(trap)
        if ones_count == trap_size:
            fitness += trap_size
        else:
            fitness += trap_size - ones_count
    return fitness

# 5. Plateau
def plateau(binary_string):
    return binary_string_length

# test the objective functions with the binary string
print("Binary String:", binary_string)
print("OneMax:", onemax(binary_string))
print("Longest 1 Chain:", longest_1_chain(binary_string))
print("Royal Road:", royal_road(binary_string))
print("Deceptive Trap:", deceptive_trap(binary_string))
print("Plateau:", plateau(binary_string))
