import openpyxl

def read_test_cases(filepath):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb.active
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        testcase, username, password, module, action, expected, extra_data = row
        data.append({
            "testcase": testcase,
            "username": username,
            "password": password,
            "module": module,
            "action": action,
            "expected": expected,
            "extra_data": extra_data
        })

    return data
