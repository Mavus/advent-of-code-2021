'''
Advent of Code 2021
Day 3: Binary Diagnostic
'''
def get_gamma_epsilon(binary_input_array):
    '''Get most and least common bits in a list of binary digits.'''
    input_length = len(binary_input_array)
    gamma_bit_count = [0]*len(binary_input_array[0])

    for binary_digit in binary_input_array:
        for bit_position in range(len(binary_digit)):
            gamma_bit_count[bit_position] += int(binary_digit[bit_position])
    
    gamma_rate = "".join(['1' if bit_count > input_length/2 else '0' for bit_count in gamma_bit_count])
    gamma_rate = int(gamma_rate, base=2)
    epsilon_rate = "".join(['0' if bit_count > input_length/2 else '1' for bit_count in gamma_bit_count])
    epsilon_rate = int(epsilon_rate, base=2)
    return gamma_rate, epsilon_rate

def part1(gamma, epsilon):
    '''Return power consumption. The product of gamma and epsilon rates.'''
    return gamma_rate * epsilon_rate

def part2(binary_input_array):
    '''Get'''
    input_length = len(binary_input_array)
    bit_array_length = len(binary_input_array[0])
    most_common_bit_count = [0]*bit_array_length
    least_common_bit_count = [0]*bit_array_length
    filtered_oxygen_generator_array = binary_input_array
    filtered_co2_scrubber_array = binary_input_array
    for i in range(bit_array_length):
        print(f"index {i}")
        for binary_digit in filtered_oxygen_generator_array:
            most_common_bit_count[i] += int(binary_digit[i])
        for binary_digit in filtered_co2_scrubber_array:
            least_common_bit_count[i] += int(binary_digit[i])
        most_common_bit = 1 if most_common_bit_count[i] >= len(filtered_oxygen_generator_array)/2 else 0
        least_common_bit = 1 if least_common_bit_count[i] < len(filtered_co2_scrubber_array)/2 else 0
        print(f"least common bit {least_common_bit}")
        filtered_oxygen_generator_array = [binary_digit for binary_digit in filtered_oxygen_generator_array if int(binary_digit[i]) == most_common_bit]
        filtered_co2_scrubber_array = [binary_digit for binary_digit in filtered_co2_scrubber_array if int(binary_digit[i]) == least_common_bit]
        print(filtered_co2_scrubber_array)
        if len(filtered_oxygen_generator_array) == 1:
            oxygen_generator_rating = int(filtered_oxygen_generator_array[0], base=2)        
        if len(filtered_co2_scrubber_array) == 1:
            co2_scrubber_rating = int(filtered_co2_scrubber_array[0], base=2)
    return oxygen_generator_rating * co2_scrubber_rating

if __name__ == "__main__":
    with open('input.txt', encoding='utf-8') as input_file:
        diagnostic_report = input_file.read().split('\n')
        gamma_rate, epsilon_rate = get_gamma_epsilon(diagnostic_report)
        print(part1(gamma_rate, epsilon_rate))
        print(part2(diagnostic_report))