def to_binary(n,bits=8):
    return format(n&(2**bits-1),f'0{bits}b')

def from_binary(b):
    return int(b,2)

def twos_complement(value, bits=8):
    value &=(2**bits-1)
    return format(value,f'0{bits}b')