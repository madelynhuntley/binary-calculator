def bin_to_dec(bin_str):
    reversed = bin_str[::-1]
    sum = 0
    for idx, value in enumerate(reversed):
        sum += int((value))*2**idx
    return(sum)


def dec_to_bin(dec_num):
    dec_num = int(dec_num)
    place_val = [128, 64, 32, 16, 8, 4, 2, 1]
    binarynum = []
    
    for place in place_val:
        if (dec_num >= place):
            binarynum.append('1')
            dec_num -= place 
        else:
            binarynum.append('0')
    return "".join(binarynum)
    

def bin_add(bin_add_1, bin_add_2):
    max_length = max(len(bin_add_1),len(bin_add_2))
    bin_add_1, bin_add_2 = [
        list(bin_add_1.zfill(max_length)[::-1]),
        list(bin_add_2.zfill(max_length)[::-1]),
    ] 
    sum = []
    for bit in range(len(bin_add_2)):
        sum.append(int(bin_add_1[bit]) + int(bin_add_2[bit]))
    
    for i, num in enumerate(sum):
        if num > 1:
            sum[i] -= 2
            if i + 1 > len(sum)-1:
                sum.append(0)
                sum[i+1] += 1
            else:
                sum[i + 1] += 1
        sum[i] = str(sum[i])
    return "".join(sum[::-1])



def bin_sub(bin_sub1,bin_sub2):
    max_length = max(len(bin_sub1),len(bin_sub2))

    greater = bin_sub1 if bin_sub1 > bin_sub2 else bin_sub2
    
    lesser = bin_sub1 if bin_sub1 < bin_sub2 else bin_sub2
   
    greater, lesser = [
        list(greater.zfill(max_length))[::-1], 
        list(lesser.zfill(max_length))[::-1],
    ]
    results = [] 

    for bit in range(len(lesser)):
        results.append(int(greater[bit]) - int(lesser[bit]))

    for i, num in enumerate(results):
        if num < 0:
            results[i] += 2 
            results[i+1]-= 1
        results[i] = str(results[i])
    return "".join(results[::-1])


def bin_mul(bin_mul_1,bin_mul_2):
    bin_mul_list_1 = ["0","0","0","0","0","0","0","0"]
    bin_mul_list_result = []
    carryover = 0

    result = int(bin_mul_1) * int(bin_mul_2)
    result = str(result)
    
    for i in result:
        bin_mul_list_1.append(i)
    
    bin_mul_list_1.reverse()
    
    for i in range(len(bin_mul_list_1)):
        sum = int(bin_mul_list_1[i]) + carryover
    
        if sum == 0:
            bin_mul_list_result.append("0")
            carryover = 0

        elif sum == 1:
            bin_mul_list_result.append("1")
            carryover = 0
            
        elif sum == 2:
            bin_mul_list_result.append("0")
            carryover = 1

        elif sum == 3:
            bin_mul_list_result.append("1")
            carryover = 1

        elif sum == 4:
            bin_mul_list_result.append("0")
            carryover = 2

        elif sum == 5:
            bin_mul_list_result.append("1")
            carryover = 2

    bin_mul_list_result.reverse()
    return "".join(bin_mul_list_result)  


def bin_div(dividend,divisor):
    # max_length = max(len(dividend),len(divisor))
    
    current = ""
    previous = ""
    result =  ""
    
    for bit in dividend:
        previous += bit
        max_prev = max(len(previous),len(divisor))
        previous = previous.zfill(max_prev)
        divisor = divisor.zfill(max_prev)
       
        if divisor <= previous:
            result += '1'
            current = divisor
            # previous = bin_sub(previous,current)

        else:
            result += '0'
            current = '0'
        previous = bin_sub(previous, current)
    return result


def bin_inverse(bin_str):
    bin_inverse = ''
    if bin_str[0] == '1':
        bin_str = f'0{bin_str}'

    for bit in bin_str: 
        if bit == '0': 
            bin_inverse+='1'
        elif bit == '1':
            bin_inverse += '0'
    neg_bin = bin_add(bin_inverse,'1')
    return neg_bin
            






while True:
    print("    *** Binary Calculator ***")
    print("----------------------------------")
    menu_select = int(input("(1) Binary to Decimal Conversion\n(2) Decimal to Binary Conversion\n(3) Add two Binary Numbers\n(4) Subtract two Binary Numbers\n(5) Multiply two Binary Numbers\n(6) Divide two Binary Numbers\n(7) Convert binary to 2's compliment\n(8) Quit\n"))

 
    if menu_select == 1:
        bin_str = input("Enter a Binary number to convert to Decimal:").replace(" ","")
        print(bin_to_dec(bin_str))

        
    elif menu_select == 2:
        dec_num = input("Enter a Number to convert to Binary:").replace(" ","")
        print(dec_to_bin(dec_num))

    elif menu_select == 3: 
        bin_add_1 = input("Enter the first Binary number you would like add:").replace(" ", "")
        bin_add_2 = input("Enter the second Binary number you would like add:").replace(" ","")
        print(bin_add(bin_add_1, bin_add_2))

    elif menu_select == 4:
        bin_sub1 = input("Enter the first Binary number:").replace(" ", "")
        bin_sub2 = input("Enter the subtracting Binary number:").replace(" ","")
        print(bin_sub(bin_sub1, bin_sub2))

    elif menu_select == 5:
        bin_mul_1 = input("Enter the first Binary number to multiply:").replace(" ","")
        bin_mul_2 = input("Enter the second Binary number to multiply:").replace(" ","")
        print(bin_mul(bin_mul_1, bin_mul_2))

    elif menu_select == 6:
        bin_div_1 = input("Enter the first Binary number:").replace(" ","")
        bin_div_2 = input("Enter the dividing Binary number:").replace(" ","")
        print(bin_div(bin_div_1, bin_div_2))
    
    elif menu_select == 7: 
        bin_str = input("Enter the binary number you would like converted to 2's compliment. ")
        print(bin_inverse(bin_str))

    elif menu_select == 8:
        print("Thank you.")
        break

    else:
        exit()

  



