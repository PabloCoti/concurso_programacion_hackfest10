# Open file and extract its content
file = open('data.txt')
file_content = file.read()

# Sort the numbers within their rectangles and insert them into a list for easier management
rectangles = []

file_rows = file_content.split('\n')

for r in file_rows:
    row = []
    if r != '':
        file_columns = r.split(',')

        for c in file_columns:
            if '.' in c or int(c) < 0 or len(file_columns) != 4:
                raise Exception('Wrong number format')

            else:
                row.append(int(c))

        rectangles.append(row)

# Check for intersections
intersections = []

for r1 in rectangles:
    intersection = []

    for r2 in rectangles:
        if r1 != r2:
            for c in range(3):
                if r1[c] == r2[c] and r1[c+1] == r2[c+1]:
                    intersection.append(r1)
                    intersection.append(r2)

                    temp = [intersection[1], intersection[0]]
                    if intersection not in intersections and temp not in intersections:
                        intersections.append(intersection)

# Calculate the area
areas = []
i_areas = []

for r in rectangles:
    print(r)
    base = r[2]-r[0]
    height = r[3]-r[1]
    area = base*height

    areas.append(area)

    for i in intersections:
        if r in i:
            print(i)
            i_base = i[1][2] - i[1][0]
            i_height = i[1][3] - i[1][1]

            r_base = min(base, i_base)
            r_height = min(height, i_height)

            i_area = r_base*r_height
            i_areas.append(i_area)

            intersections.remove(i)
            break



total = 0
for a in areas:
    total += a

for ia in i_areas:
    total -= ia

print(f"Area total: {total}")
