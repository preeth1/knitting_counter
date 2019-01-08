from datetime import datetime


def print_count(pattern):
    print("Press any key to advance to the next line in the pattern.")
    for line in pattern:
        input("")
        print("Pattern advanced at: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
        print(line)

def round_heel(first_purl_stitches):
    # http://www.socknitters.com/Tips/heels_by_the_number.htm
    stitch_num = 4
    round_heel_56_list = [
        'slip 1, knit {}, SSK, K1, turn'.format(first_purl_stitches),
    ]

    while stitch_num != 20:
        stitch_num += 1
        line_to_add = 'slip 1, purl {}, p2tog, P1, turn'.format(stitch_num),

        round_heel_56_list.append(line_to_add)

        stitch_num += 1
        line_to_add = 'slip 1, knit {}, SSK, K1, turn'.format(stitch_num),

        round_heel_56_list.append(line_to_add)

    return round_heel_56_list

if __name__ == "__main__":
    hand_top_deacrease = [
        "Rnd 1: *K4, k2tog; rep from * around - 30 sts.",
        "Rnd 2: Knit.",
        "Rnd 3: *K3, k2tog; rep from * around - 24 sts.",
        "Rnd 4: Knit.",
        "Rnd 5: *K2, k2tog; rep from * around - 18 sts.",
        "Rnd 6: Knit.",
        "Rnd 7: *K1, k2tog; rep from * around - 12 sts.",
        "Rnd : Knit.",
        "Rnd 9: K2tog around - 6 sts.",
    ]
    kitchener = [
        "Setup: Front purl on",
        "Setup: Back knit on",
        "Front knit off",
        "Front purl on",
        "Back purl off",
        "Back knit on",
        "Front knit off",
        "Front purl on",
        "Back purl off",
        "Back knit on",
        "Front knit off",
        "Front purl on",
        "Back purl off",
        "Back knit on",
        "Front knit off",
        "Front purl on",
        "Back purl off",
        "Back knit on",
        "Front knit off",
        "Front purl on",
        "Back purl off",
        "Back knit on",
        "Front knit off",
        "Front purl on",
        "Back purl off",
        "Back knit on",
    ]


    print_count(kitchener)
