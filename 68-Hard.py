## Text Justification

## Given an array of strings words and a width maxWidth, format the text such that 
## each line has exactly maxWidth characters and is fully (left and right) justified.

def fullJustify(words, maxWidth):
    result=[]

    total_char=0
    word_count=0
    temp=[]
    for word in words:
        if total_char+len(word)>maxWidth:
            space=maxWidth-total_char+word_count
            added=0
            j=0
            while(added<space):
                #print(j)
                #print(len(temp)-1)
                if (j>=(len(temp)-1)):
                    j=0
                #print(temp[j])
                temp[j] += ' '
                added +=1
                j+=1
            result.append(''.join(temp))
            temp=[]
            temp.append(word)
            total_char=len(word)+1
            word_count=1
        else:
            total_char+=len(word)
            total_char+=1
            temp.append(word)
            word_count+=1
    space=maxWidth-total_char+1
    temp[-1] += ' '*space
    result.append(' '.join(temp))
    return result

if __name__=='__main__':
    maxWidth=16
    words=["This", "is", "an", "example", "of", "text", "justification."]
    print(fullJustify(words, maxWidth))