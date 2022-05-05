from openpyxl import load_workbook
from class_element_for_tree import BinaryTreeElement
from tkinter import *


def place_the_item_in_a_tree(element: BinaryTreeElement, position_x: int, position_y: int) -> None:
    if element.return_best_main_premise() is not None and element.find_best_entropy() is not None:
        print(element.return_conclusion_tab())
        element.calculate_conclusion_entropy()
        element.return_entropy_tab()
        element.return_information_gain()
        print(f"Max(I-Ej): {element.return_best_main_premise()} {element.find_best_entropy()}")
        element.draw_element_on_tree(position_x=position_x, position_y=position_y)
        # print(element.return_left_branch())
        # print(element.return_right_branch())
        print(element)


def create_an_option_to_table(sheet, min_row: int, min_col: int, max_row: int, max_col: int, table=None):
    if table is None:
        table = []
    for col in sheet.iter_cols(min_row=min_row, min_col=min_col, max_row=max_row, max_col=max_col):
        for cell in col:
            if cell.value is not None:
                table.append(cell.value)
    return table


def run_example():
    wb = load_workbook("Test.xlsx")

    sheet = wb.active

    premises = {}
    one_hundred_examples = {}

    option_of_premises = create_an_option_to_table(sheet, 2, 2, 16, 2)
    option_of_conclusion = create_an_option_to_table(sheet, 18, 1, 20, 1)

    for value in range(100):
        one_hundred_examples[value] = {}

    for col in sheet.iter_cols(min_row=2, min_col=1, max_row=14, max_col=1):
        for cell in col:
            if cell.value is not None:
                premises[cell.value] = ""

    for number, col in enumerate(sheet.iter_cols(min_row=2, min_col=3, max_row=20, max_col=102)):
        for index, cell in enumerate(col):
            if cell.value is not None:
                if 0 <= index <= 3:
                    premises["wiek"] = option_of_premises[index]
                elif 4 <= index <= 5:
                    premises["płeć"] = option_of_premises[index]
                elif 6 <= index <= 8:
                    premises["zar. mies."] = option_of_premises[index]
                elif 9 <= index <= 11:
                    premises["ost. posiłek"] = option_of_premises[index]
                elif 12 <= index <= 14:
                    premises["os. spoż. pizze"] = option_of_premises[index]
                elif 16 <= index <= 18:
                    premises["konkluzja(wybór pizzy):"] = option_of_conclusion[index - 16]
                    one_hundred_examples[number].update(premises)

    # for key, value in one_hundred_examples.items():
    #     print(f"{key} : {value}")

    window = Tk()
    window.geometry('2048x1024+0+0')
    window.title("Drzewo decyzyjne")
    conclusion = "konkluzja(wybór pizzy):"
    main_premises = list(premises.keys())

    """"" Binary tree: N - node, R - right, L - left (L and R means the direction of movement in the tree) """

    """ LEVEL 0 """

    N = BinaryTreeElement(one_hundred_examples, conclusion, main_premises, option_of_premises,
                          option_of_conclusion, window)

    """ LEVEL 1 """

    L = BinaryTreeElement(N.return_left_branch(), conclusion, main_premises, option_of_premises,
                          option_of_conclusion, window)
    R = BinaryTreeElement(N.return_right_branch(), conclusion, main_premises, option_of_premises,
                          option_of_conclusion, window)

    """ LEVEL 2 """

    LL = BinaryTreeElement(L.return_left_branch(), conclusion, main_premises, option_of_premises,
                           option_of_conclusion, window)

    LR = BinaryTreeElement(L.return_right_branch(), conclusion, main_premises, option_of_premises,
                           option_of_conclusion, window)

    RR = BinaryTreeElement(R.return_right_branch(), conclusion, main_premises, option_of_premises,
                           option_of_conclusion, window)

    RL = BinaryTreeElement(R.return_left_branch(), conclusion, main_premises, option_of_premises,
                           option_of_conclusion, window)

    """ LEVEL 3 """

    LRL = BinaryTreeElement(LR.return_left_branch(), conclusion, main_premises, option_of_premises,
                            option_of_conclusion, window)

    LRR = BinaryTreeElement(LR.return_right_branch(), conclusion, main_premises, option_of_premises,
                            option_of_conclusion, window)

    RLL = BinaryTreeElement(RL.return_left_branch(), conclusion, main_premises, option_of_premises,
                            option_of_conclusion, window)

    RLR = BinaryTreeElement(RL.return_right_branch(), conclusion, main_premises, option_of_premises,
                            option_of_conclusion, window)

    RRL = BinaryTreeElement(RR.return_left_branch(), conclusion, main_premises, option_of_premises,
                            option_of_conclusion, window)

    RRR = BinaryTreeElement(RR.return_right_branch(), conclusion, main_premises, option_of_premises,
                            option_of_conclusion, window)

    """ LEVEL 4 """

    LRRL = BinaryTreeElement(LRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    LRRR = BinaryTreeElement(LRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    RLRL = BinaryTreeElement(RLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    RLRR = BinaryTreeElement(RLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    RRLL = BinaryTreeElement(RRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    RRLR = BinaryTreeElement(RRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    RRRL = BinaryTreeElement(RRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    RRRR = BinaryTreeElement(RRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                             option_of_conclusion, window)

    """ LEVEL 5 """

    LRRLL = BinaryTreeElement(LRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    LRRLR = BinaryTreeElement(LRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    LRRRL = BinaryTreeElement(LRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    LRRRR = BinaryTreeElement(LRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RLRRL = BinaryTreeElement(RLRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RLRRR = BinaryTreeElement(RLRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RRLLL = BinaryTreeElement(RRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RRLLR = BinaryTreeElement(RRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RRLRL = BinaryTreeElement(RRLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RRLRR = BinaryTreeElement(RRLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RRRRL = BinaryTreeElement(RRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    RRRRR = BinaryTreeElement(RRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                              option_of_conclusion, window)

    """ LEVEL 6 """

    LRRLLL = BinaryTreeElement(LRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)

    LRRLLR = BinaryTreeElement(LRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)

    LRRRLL = BinaryTreeElement(LRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)

    LRRRLR = BinaryTreeElement(LRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)

    LRRRRL = BinaryTreeElement(LRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)

    LRRRRR = BinaryTreeElement(LRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RLRRLL = BinaryTreeElement(RLRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RLRRLR = BinaryTreeElement(RLRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RLRRRL = BinaryTreeElement(RLRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RLRRRR = BinaryTreeElement(RLRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRLLLL = BinaryTreeElement(RRLLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRLLLR = BinaryTreeElement(RRLLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRLRRL = BinaryTreeElement(RRLRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRLRRR = BinaryTreeElement(RRLRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRRRLL = BinaryTreeElement(RRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRRRLR = BinaryTreeElement(RRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRRRRL = BinaryTreeElement(RRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)
    RRRRRR = BinaryTreeElement(RRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                               option_of_conclusion, window)

    """ LEVEL 7 """

    LRRLLLL = BinaryTreeElement(LRRLLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    LRRLLLR = BinaryTreeElement(LRRLLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    LRRRLLL = BinaryTreeElement(LRRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    LRRRLLR = BinaryTreeElement(LRRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    LRRRRLL = BinaryTreeElement(LRRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    LRRRRLR = BinaryTreeElement(LRRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RLRRLRL = BinaryTreeElement(RLRRLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RLRRLRR = BinaryTreeElement(RLRRLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RLRRRRL = BinaryTreeElement(RLRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RLRRRRR = BinaryTreeElement(RLRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRLLLRL = BinaryTreeElement(RRLLLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRLLLRR = BinaryTreeElement(RRLLLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRLRRLL = BinaryTreeElement(RRLRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRLRRLR = BinaryTreeElement(RRLRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRLRRRL = BinaryTreeElement(RRLRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRLRRRR = BinaryTreeElement(RRLRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRRRLLL = BinaryTreeElement(RRRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRRRLLR = BinaryTreeElement(RRRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRRRRLL = BinaryTreeElement(RRRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRRRRLR = BinaryTreeElement(RRRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRRRRRL = BinaryTreeElement(RRRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)
    RRRRRRR = BinaryTreeElement(RRRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                option_of_conclusion, window)

    """ LEVEL 8 """

    RRRRRRLL = BinaryTreeElement(RRRRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                 option_of_conclusion, window)
    RRRRRRLR = BinaryTreeElement(RRRRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                 option_of_conclusion, window)
    RRRRRLLL = BinaryTreeElement(RRRRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                 option_of_conclusion, window)
    RRRRRLLR = BinaryTreeElement(RRRRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                 option_of_conclusion, window)

    leaves = ((N, 800, 0), (L, 200, 50), (R, 1100, 50), (LL, 100, 100), (LR, 290, 100), (RR, 1400, 100),
              (RL, 900, 100), (LRL, 250, 150), (LRR, 400, 150), (RLL, 850, 150), (RLR, 950, 150), (RRL, 1350, 150),
              (RRR, 1520, 150), (LRRL, 200, 200), (LRRR, 600, 200), (RLRL, 900, 200), (RLRR, 960, 200),
              (RRLL, 1300, 200), (RRLR, 1420, 200), (RRRL, 1500, 200), (RRRR, 1630, 200), (LRRLL, 150, 250),
              (LRRLR, 320, 250), (LRRRL, 450, 250), (LRRRR, 640, 250), (RLRRL, 800, 250), (RLRRR, 1000, 250),
              (RRLLL, 1200, 250), (RRLLR, 1330, 250), (RRLRL, 1385, 250), (RRLRR, 1440, 250), (RRRRL, 1570, 250),
              (RRRRR, 1730, 250), (LRRLLL, 120, 300), (LRRLLR, 180, 300), (LRRRLL, 370, 300), (LRRRLR, 530, 300),
              (LRRRRL, 570, 300), (LRRRRR, 700, 300), (RLRRLL, 765, 300), (RLRRLR, 850, 300), (RLRRRL, 950, 300),
              (RLRRRR, 1060, 300), (RRLLLL, 1150, 300), (RRLLLR, 1220, 300), (RRLRRL, 1340, 300), (RRLRRR, 1450, 300),
              (RRRRLL, 1560, 300), (RRRRLR, 1660, 300), (RRRRRL, 1710, 300), (RRRRRR, 1790, 300), (LRRLLLL, 80, 350),
              (LRRLLLR, 140, 350), (LRRRLLL, 350, 350), (LRRRLLR, 400, 350), (LRRRRLL, 500, 350), (LRRRRLR, 660, 350),
              (RLRRLRL, 780, 350), (RLRRLRR, 890, 350), (RLRRRRL, 1000, 350), (RLRRRRR, 1100, 350),
              (RRLLLRL, 1180, 350), (RRLLLRR, 1250, 350), (RRLRRLL, 1320, 350), (RRLRRLR, 1380, 350),
              (RRLRRRL, 1440, 350), (RRLRRRR, 1500, 350), (RRRRLLL, 1550, 350), (RRRRLLR, 1600, 350),
              (RRRRRLL, 1650, 350), (RRRRRLR, 1737, 350), (RRRRRRL, 1785, 350), (RRRRRRR, 1860, 350),
              (RRRRRRLL, 1750, 400), (RRRRRRLR, 1820, 400), (RRRRRLLL, 1600, 400), (RRRRRLLR, 1700, 400))

    for leave in leaves:
        place_the_item_in_a_tree(leave[0], leave[1], leave[2])



    """ Legend for the binary tree"""

    salary = Label(window, text="zar. mies. - zarobki miesięczne danej osoby",
                   font=("Times New Roman", 15))

    meals = Label(window, text="ost. posiłek - czas od ostatniego posiłku danej osoby",
                  font=("Times New Roman", 15))

    persons_eating = Label(window, text="os. spoż. pizze - liczba osób spożywających pizzę",
                           font=("Times New Roman", 15))

    meals.place(x=50, y=520)
    salary.place(x=50, y=500)
    persons_eating.place(x=50, y=540)

    # exceptions test:
    # left_left_left_leaf = BinaryTreeElement(LL.return_left_branch(), conclusion, main_premises,
    #                                         option_of_premises, option_of_conclusion, window)
    # place_the_item_in_a_tree(left_left_left_leaf, position_x=800, position_y=500)
    window.mainloop()


if __name__ == "__main__":
    run_example()
