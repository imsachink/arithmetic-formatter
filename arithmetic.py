def arithmetic_arranger(problems, show_answers=False):
    solved = []
    dashes = []
    operators = []
    final_output = []
    first_final = []
    second_final = []
    # problems are greater than 5
    if len(problems) > 5:
        return('Error: Too many problems.')
    # checking for operator
    operators = list(map(lambda x: x.split()[1], problems))
    # print(operators)
    if "/" in operators or "*" in operators:
        return ("Error: Operator must be '+' or '-'.")

    first = list(map(lambda x: x.split()[0], problems))
    second = list(map(lambda x: x.split()[2], problems))
    # check for digit
    for num in range(len(first)):
        if not first[num].isdigit() or not second[num].isdigit():
            return('Error: Numbers must only contain digits.')
            
    # check length of operands
    for char in range(len(first)):
        if len(first[0]) > 4 or len(second[0]) > 4:
            return('Error: Numbers cannot be more than four digits.')
        
            
    for char in range(len(problems)):
        width = (max(len(first[char]), len(second[char])) + 2)
        dashes.append('-' * width)
        # print(dashes)
        solved.append(f"{str(eval(problems[char])).rjust(width)}")
        first_final.append(f"{first[char].rjust(width)}")
        second_final.append(f"{operators[char]}{second[char].rjust(width - 1)}")
    if show_answers:
        final_output = ('    '.join(first_final) + '\n' + '    '.join(second_final) + '\n' + '    '.join(
            dashes) + '\n' + '    '.join(solved))
    else:
        final_output = ('    '.join(first_final) + '\n' + '    '.join(second_final) + '\n' + '    '.join(dashes))
    return final_output

#call function
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
