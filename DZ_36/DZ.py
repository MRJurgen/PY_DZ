
def print_operation_table(operation, num_rows=6, num_columns=6):
    result = []
    for i in range(num_rows):
        for j in range(num_columns):
            result.append(operation(i+1,j+1))
        print(*result)
        result = []
    
print_operation_table(lambda x, y: x*y)