Waldo = 'W'
Other = '.'


def all_row_exists_waldo(matrix: list[list[str]]) -> bool:
    """For all rows in matrix, there exists a Waldo in the row"""
    for row in range(len(matrix)):
        if len(matrix[row]) == 0:
            return False
        waldo_in_row = False
        for col in range(len(matrix[row])):
            if matrix[row][col] == Waldo:
                waldo_in_row = True
                break
            elif col == len(matrix[row]) - 1 and waldo_in_row == False:
                return False
    return True


def all_col_exists_waldo(matrix: list[list[str]]) -> bool:
    """For all columns in the matrix, there exists a Waldo in the column"""
    diff_columns = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == Waldo and col not in diff_columns:
                diff_columns.append(col)
        if len(diff_columns) != len(matrix[row]) and row == len(matrix) - 1:
            return False
    return True


def all_row_all_waldo(matrix: list[list[str]]) -> bool:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == Other:
                return False
    return True


def all_col_all_waldo(matrix: list[list[str]]) -> bool:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == Other:
                return False
    return True


def exists_row_all_waldo(matrix: list[list[str]]) -> bool:
    for row in range(len(matrix)):
        if len(matrix[row]) == 0:
            return True
        all_col = True
        for col in range(len(matrix)):
            if matrix[row][col] != Waldo:
                all_col = False
        if all_col:
            return True
    return False


def exists_col_all_waldo(matrix: list[list[str]]) -> bool:
    if len(matrix) == 0:
        return False
    impossible_columns = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != Waldo and col not in impossible_columns:
                impossible_columns.append(col)
        if len(impossible_columns) == len(matrix[row]):
            return False
    return True


def exists_row_exists_waldo(matrix: list[list[str]]) -> bool:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == Waldo:
                return True
    return False


def exists_col_exists_waldo(matrix: list[list[str]]) -> bool:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == Waldo:
                return True
    return False
