import csv


def setup(file_path, s_width, s_height, x_sections, y_sections):
    data = []
    len_seq = []
    targets_real = []
    targets_expected = []
    with open(file_path, 'r') as csvfile:
        datareader = list(csv.reader(csvfile))
        num_rows = len(datareader)

        cur_trial = 1
        len_trial = 1
        for i in range(1, num_rows):
            row = datareader[i]
            print(row[0])
            trial = int(row[0])
            x = float(row[1])
            y = float(row[2])
            fixation = [x, y]
            data.append(fixation)

            target_x = float(row[3])
            target_y = float(row[4])
            target = [target_x, target_y]
            targets_real.append(target)

            target_ex_x = float(row[5])
            target_ex_y = float(row[6])
            target_ex = [target_ex_x, target_ex_y]
            targets_expected.append(target_ex)

            if trial > cur_trial:
                cur_trial = trial
                len_seq.append(len_trial)
                len_trial = 1
            else:
                len_trial += 1
        len_seq.append(len_trial - 1)
    print(len_seq)

    input = bin(data, targets_real, targets_expected, s_width, s_height, x_sections, y_sections)
    print("total samples: " + str(len(input)))
    sum = 0
    for a in len_seq:
        sum = sum + a

    print("total: " + str(sum))
    return input, len_seq


def bin(fixations, targets_real, targets_expected, s_width, s_height, x_sections, y_sections):
    num_sections = x_sections * y_sections
    num_samples = len(fixations)
    x_len = s_width / x_sections
    y_len = s_height / y_sections
    sections = {}

    x1 = 0
    y1 = 0

    for i in range(1, num_sections + 1):
        title = "section" + str(i)
        sections[title] = []

    counter = 1
    for l in range(y_sections):
        for j in range(x_sections):
            title = "section" + str(counter)
            x2 = x1 + x_len
            y2 = y1 + y_len
            sections[title].append(x1)
            sections[title].append(y1)
            sections[title].append(x2)
            sections[title].append(y2)
            x1 = x2
            counter += 1
        y1 = y2
        x1 = 0
    #print(sections)
    cat_fixations = categorize(fixations, sections)
    cat_targets_real = categorize(targets_real, sections)
    cat_targets_expected = categorize(targets_expected, sections)

    #print(cat_fixations)
    #print(cat_targets_real)
    #print(cat_targets_expected)

    ret = []
    for q in range(num_samples):
        temp = []
        temp.extend(cat_fixations[q])
        temp.extend(cat_targets_real[q])
        temp.extend(cat_targets_expected[q])
        ret.append(temp)
    print(ret)
    return ret


def categorize(coords, bins):
    point_data = []

    for c in coords:
        point = []
        c_x = c[0]
        c_y = c[1]
        for key in bins:
            x1 = bins[key][0]
            y1 = bins[key][1]
            x2 = bins[key][2]
            y2 = bins[key][3]
            #print("checking " + str(c_x) + "," + str(c_y) + " in " + str(x1) + "," + str(y1) + ","+ str(x2) + "," + str(y2))

            if ((c_x >= x1) and (c_x <= x2)) and ((c_y >= y1) and (c_y <= y2)):
                point.append(1)
            else:
                point.append(0)
        #print(point)
        point_data.append(point)
    return point_data



#setup("input-data/test-input.csv")