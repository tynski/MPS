def extract_values(data):
    records = []
    record = None
    for x in data:
        value = ''
        for i in range(len(x) - 2, 0,-1):
            if x[i] == ' ':
                break
            value += x[i]
        record = float(value[::-1]) #reverse string and cast into float
        records.append(record)
    return records