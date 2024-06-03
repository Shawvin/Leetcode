# 1720. Decode XORed Array

def decode(encoded, first):
    temp=first
    for i in range(len(encoded)):
        encoded[i]^=temp
        temp=encoded[i]
    encoded.insert(0, first)
    return encoded

def decode2(encoded, first):
    encoded.insert(0, first)
    for i in range(1,len(encoded)):
        encoded[i]^=encoded[i-1]
    return encoded

if __name__=='__main__':
    encoded = [6,2,7,3]
    first = 4
    print(decode(encoded, first))