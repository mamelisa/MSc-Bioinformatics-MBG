print('Hello, today I can analyze for you up to 5 nucleotide sequences.\nPlease begin')
i = 0
for i in range(0,5):
    sequence = input('Enter the sequence:\n')
    l = len(sequence)
    if l % 3 == 0 and l >= 9:
        coding = sequence[0:3]
        stopcodon = sequence[l-3:l]
        if coding == 'ATG':
            if stopcodon == 'TAA' or stopcodon == 'TTA' or stopcodon =='TGA':
                for a in range(0, len(sequence[l-3:l]), 3): 
                    triplet = sequence[a:a+3]
                    if triplet != 'TAA' or triplet != 'TTA' or triplet != 'TGA':
                        print('This sequence is a CODING sequence')
                        break
                    else:
                        print('This is not a coding sequence')
                else:
                    print('This is not a coding sequence')
            else:
                print('This is not a coding sequence')
    else: 
        print('The sequence that you have entered is too small or not in a triplet frame')
print('I hope i have helped you!')
