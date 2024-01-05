print('Hello, ready to begin?\n')

number = int(input('How many sequences would you like to analyze today? \n'))
i = 0
num = 0


for i in range(0,number):
    sequence = input('Enter the sequence without the introns:\n')
    l = len(sequence)
    if l % 3 == 0 and l >= 15:
        coding = sequence[0:3]
        stopcodon = sequence[l-3:l]
        if coding == 'ATG' or coding == 'atg':
            if stopcodon == 'TAA' or stopcodon == 'TTA' or stopcodon =='TGA' or stopcodon == 'taa' or stopcodon == 'tta' or stopcodon =='tga' :
                for a in range(0, len(sequence[l-3:l]), 3): 
                    triplet = sequence[a:a+3]
                    if triplet != 'TAA' or triplet != 'TTA' or triplet != 'TGA' or triplet != 'taa' or triplet != 'tta' or triplet != 'tga' :
                        print('This sequence is a CODING sequence')
                        num += 1
                        break
                    else:
                        print('This is not a coding sequence')
                else:
                    print('This is not a coding sequence')
            else:
                print('This is not a coding sequence.There is no stop codon')
        else:
            print('This is not a coding sequence. The coding sequence should start with an ATG')
    else:
        print('The sequence that you have entered is too small or not in a triplet frame')
print('The total amount of coding sequences was:', num)
print('The coding region of some genes is in the reverse complementary strand. \nIn order to be sure that the sequences you have typed are coding, you might want to use a more advance program.\nI hope i have helped you!')
