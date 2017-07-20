# ONLY WORKS IN PYTHON 3

# Out of date but cool idea, so maybe you should fix this.
# Could also add possibility to pass ALA(QBLA) scores as input.

# You have to convert your raw WAB scores as follows (the script accepts only integer inputs)
# Fluency: no changes
# Comprehension: out of 1000 instead of out of 100.
# Repetition: out of 100 instead of out of 10.
# Naming: out of 100 instead of out of 10.

import csv
with open('wab.csv') as f:
    csv_f = csv.DictReader(f) # parses the file as a list of rows

    for row in csv_f:
        # print(row['fluency'], row['comprehension'], row['repetition'], row['naming'])

        try:
            fl = int(row['fluency'])
            co = int(row['comprehension'])
            re = int(row['repetition'])
            na = int(row['naming'])
        except Exception as e:
            # print('could not convert values to integers (%s)! ... skipping' % e)
            print('-')
            continue

        if fl > 4:
            if co >= 700:
                if re >= 70:
                    if na >= 90:
                        print("WNL")
                    else:
                        print("Anomic")
                else:
                    if na >= 90:
                        print("Unclassifiable")
                    else:
                        print("Conduction")
            else:
                if re >= 80:
                    if na >= 90:
                        print("Unclassifiable")
                    else:
                        print("Trans Sensory")
                else:
                    if na >= 90:
                        print("Unclassifiable")
                    else:
                        print("Wernicke's")
        else:
            if co >= 400:
                if re >= 80:
                    if na >= 80 and na <= 10:
                        print("Unclassifiable")
                    else:
                        print("Trans Motor")
                else:
                    if na >= 80:
                        print("Unclassifiable")
                    else:
                        print("Broca's")
            else:
                if re >= 50:
                    if na >= 60:
                        print("Unclassifiable")
                    else:
                        print("Isolation")
                else:
                    if na >= 60:
                        print("Unclassifiable")
                    else:
                        print("Global")

        #################################################
        # OLD EXAMPLE:
        # if fl <= 5:
        #     print("It's Broca's aphasia!")
        # else:
        #     print("It's Wernicke's aphasia!")
        ################################################
