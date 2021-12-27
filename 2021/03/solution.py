def read_text_lines(fp):
    with open(fp) as f:
        lines = f.read().splitlines()
    return lines

def calc_bit_freqs(data):
    freq_dict = {}
    # keep a dictionary of counts for the binary values at each column position
    for byte in data:
        for col, bit in enumerate(byte):
            bit = int(bit)
            # update with the count
            try:
                current_count = freq_dict[col][bit]
                freq_dict[col][bit] = current_count + 1
            except KeyError:
                # cold start
                freq_dict[col] = {0: 0, 1: 1}
                freq_dict[col][bit] = 1
    return freq_dict

def construct_bit_string(freq_dict, occurance):
    # need to find most or least common byte in each column bit position
    bit_str = ''

    if occurance == 'most':
        # used to calculate gamma rate
        for col, freqs in freq_dict.items():
            if freqs[0] > freqs[1]:
                bit_str += '0'
            else:
                bit_str += '1'

    elif occurance == 'least':
        # condition simply flips for calculating epsilon rate
        for col, freqs in freq_dict.items():
            if freqs[0] < freqs[1]:
                bit_str += '0'
            else:
                bit_str += '1'

    return bit_str

def calc_power_consumption(data):
    freq_dict = calc_bit_freqs(data)

    gamma_bit_str = construct_bit_string(freq_dict, occurance='most')
    gamma_rate =  int(gamma_bit_str, 2)
    print('# gamma rate', gamma_rate)

    epsilon_bit_str = construct_bit_string(freq_dict, occurance='least')
    epsilon_rate = int(epsilon_bit_str, 2)
    print('# epsilon rate', epsilon_rate)

    return gamma_rate * epsilon_rate

def calc_part2_freq(data, col_idx, occurance):
    n_zeroes = 0
    n_ones = 0
    for dat in data:
        if dat[col_idx] == '0':
            n_zeroes += 1
        else:
            n_ones += 1
    
    if occurance == 'most':
        if n_zeroes > n_ones:
            soln = '0'
        elif (n_zeroes < n_ones) or (n_zeroes == n_ones):
            soln = '1'

    elif occurance == 'least':
        if n_zeroes < n_ones or (n_zeroes == n_ones):
            soln = '0'
        elif (n_zeroes > n_ones):
            soln = '1'
    
    return soln

def bit_criteria_calc(data, occurance):
    discarded = set()
    for col_idx in range(len(data[0])):
        # calculate frequency according to criterion
        remaining = list(set(data) - discarded)
        bit_cond = calc_part2_freq(remaining, col_idx, occurance)
        for byte in remaining:
            if len(remaining) > 1:
                # if we haven't found the answer, check remaining data against criteria
                if byte[col_idx] != bit_cond:
                    discarded.add(byte)
    
    remaining = list(set(data) - discarded)[0]
    return remaining

def calc_life_support_rating(data):
    o2_rating = bit_criteria_calc(data, 'most')
    o2_rating = int(o2_rating, 2)
    print('# Oxygen rating is:', o2_rating)

    co2_rating = bit_criteria_calc(data, 'least')
    co2_rating = int(co2_rating, 2)
    print('# CO2 rating is:', co2_rating)

    return o2_rating * co2_rating


if __name__ == '__main__':
    data = read_text_lines('binary-data.txt')
    print('# Power consumption is:', calc_power_consumption(data))
    print('# life support rating is:', calc_life_support_rating(data))
