# -*- coding: utf-8 -*-


gene = 'AGTCAATGGAATAGGCCAAGCGAATATTTGGGCTACCA'

def freq(letter, text):
    n = 0.0
    for i in range(len(text)):
        if text[i] == letter:
            n += 1
    return n/len(text)
    
def pairs(letters, text):
    n = 0
    for i in range(len(text)):
        if text[i:i+2] == letters:
            n += 1
    return n
    
def mystruct(text):
    n = 0
    for i in range(len(text)):
        if text[i] == 'G':
            for j in range(i+1, len(text)):
                if text[j] == 'A' or text[j] == 'T':
                    continue
                elif text[j:j+2] == "GG":
                        n += 1
                        break
                else:
                        break
    return n
        
print freq('C', gene)
print freq('G', gene)    
print pairs("AA", gene)
print mystruct(gene)        
        
