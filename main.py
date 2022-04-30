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
    place_the_item_in_a_tree(N, position_x=800, position_y=0)

    """ LEVEL 1 """

    L = BinaryTreeElement(N.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(L, position_x=200, position_y=50)
    R = BinaryTreeElement(N.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)

    """ LEVEL 2 """

    place_the_item_in_a_tree(R, position_x=1100, position_y=50)
    LL = BinaryTreeElement(L.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LL, position_x=100, position_y=100)
    LR = BinaryTreeElement(L.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LR, position_x=290, position_y=100)
    RR = BinaryTreeElement(R.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RR, position_x=1400, position_y=100)
    RL = BinaryTreeElement(R.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RL, position_x=900, position_y=100)

    """ LEVEL 3 """

    LRL = BinaryTreeElement(LR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRL, position_x=250, position_y=150)
    LRR = BinaryTreeElement(LR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRR, position_x=400, position_y=150)
    RLL = BinaryTreeElement(RL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLL, position_x=850, position_y=150)
    RLR = BinaryTreeElement(RL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLR, position_x=950, position_y=150)
    RRL = BinaryTreeElement(RR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRL, position_x=1350, position_y=150)
    RRR = BinaryTreeElement(RR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRR, position_x=1520, position_y=150)

    """ LEVEL 4 """

    LRRL = BinaryTreeElement(LRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRL, position_x=200, position_y=200)
    LRRR = BinaryTreeElement(LRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRR, position_x=600, position_y=200)
    RLRL = BinaryTreeElement(RLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRL, position_x=900, position_y=200)
    RLRR = BinaryTreeElement(RLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRR, position_x=960, position_y=200)
    RRLL = BinaryTreeElement(RRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLL, position_x=1300, position_y=200)
    RRLR = BinaryTreeElement(RRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLR, position_x=1420, position_y=200)
    RRRL = BinaryTreeElement(RRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRL, position_x=1500, position_y=200)
    RRRR = BinaryTreeElement(RRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRR, position_x=1630, position_y=200)

    """ LEVEL 5 """

    LRRLL = BinaryTreeElement(LRRL.return_left_branch(), conclusion,main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRLL, position_x=150, position_y=250)
    LRRLR = BinaryTreeElement(LRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRLR, position_x=320, position_y=250)
    LRRRL = BinaryTreeElement(LRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRL, position_x=450, position_y=250)
    LRRRR = BinaryTreeElement(LRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRR, position_x=640, position_y=250)
    RLRRL = BinaryTreeElement(RLRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRL, position_x=800, position_y=250)
    RLRRR = BinaryTreeElement(RLRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRR, position_x=1000, position_y=250)
    RRLLL = BinaryTreeElement(RRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLLL, position_x=1200, position_y=250)
    RRLLR = BinaryTreeElement(RRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLLR, position_x=1330, position_y=250)
    RRLRL = BinaryTreeElement(RRLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRL, position_x=1385, position_y=250)
    RRLRR = BinaryTreeElement(RRLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRR, position_x=1440, position_y=250)
    RRRRL = BinaryTreeElement(RRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRL, position_x=1570, position_y=250)
    RRRRR = BinaryTreeElement(RRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRR, position_x=1730, position_y=250)

    """ LEVEL 6 """

    LRRLLL = BinaryTreeElement(LRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRLLL, position_x=120, position_y=300)
    LRRLLR = BinaryTreeElement(LRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRLLR, position_x=180, position_y=300)
    LRRRLL = BinaryTreeElement(LRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRLL, position_x=370, position_y=300)
    LRRRLR = BinaryTreeElement(LRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRLR, position_x=530, position_y=300)
    LRRRRL = BinaryTreeElement(LRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRRL, position_x=570, position_y=300)
    LRRRRR = BinaryTreeElement(LRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRRR, position_x=700, position_y=300)
    RLRRLL = BinaryTreeElement(RLRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRLL, position_x=765, position_y=300)
    RLRRLR = BinaryTreeElement(RLRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRLR, position_x=850, position_y=300)
    RLRRRL = BinaryTreeElement(RLRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRRL, position_x=950, position_y=300)
    RLRRRR = BinaryTreeElement(RLRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRRR, position_x=1060, position_y=300)
    RRLLLL = BinaryTreeElement(RRLLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLLLL, position_x=1150, position_y=300)
    RRLLLR = BinaryTreeElement(RRLLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLLLR, position_x=1220, position_y=300)
    RRLRRL = BinaryTreeElement(RRLRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRRL, position_x=1340, position_y=300)
    RRLRRR = BinaryTreeElement(RRLRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRRR, position_x=1450, position_y=300)
    RRRRLL = BinaryTreeElement(RRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRLL, position_x=1560, position_y=300)
    RRRRLR = BinaryTreeElement(RRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRLR, position_x=1660, position_y=300)
    RRRRRL = BinaryTreeElement(RRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRL, position_x=1710, position_y=300)
    RRRRRR = BinaryTreeElement(RRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRR, position_x=1790, position_y=300)

    """ LEVEL 7 """

    LRRLLLL = BinaryTreeElement(LRRLLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRLLLL, position_x=80, position_y=350)
    LRRLLLR = BinaryTreeElement(LRRLLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRLLLR, position_x=140, position_y=350)
    LRRRLLL = BinaryTreeElement(LRRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRLLL, position_x=350, position_y=350)
    LRRRLLR = BinaryTreeElement(LRRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRLLR, position_x=400, position_y=350)
    LRRRRLL = BinaryTreeElement(LRRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRRLL, position_x=500, position_y=350)
    LRRRRLR = BinaryTreeElement(LRRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(LRRRRLR, position_x=660, position_y=350)
    RLRRLRL = BinaryTreeElement(RLRRLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRLRL, position_x=780, position_y=350)
    RLRRLRR = BinaryTreeElement(RLRRLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRLRR, position_x=890, position_y=350)
    RLRRRRL = BinaryTreeElement(RLRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRRRL, position_x=1000, position_y=350)
    RLRRRRR = BinaryTreeElement(RLRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RLRRRRR, position_x=1100, position_y=350)
    RRLLLRL = BinaryTreeElement(RRLLLR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLLLRL, position_x=1180, position_y=350)
    RRLLLRR = BinaryTreeElement(RRLLLR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLLLRR, position_x=1250, position_y=350)
    RRLRRLL = BinaryTreeElement(RRLRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRRLL, position_x=1320, position_y=350)
    RRLRRLR = BinaryTreeElement(RRLRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRRLR, position_x=1380, position_y=350)
    RRLRRRL = BinaryTreeElement(RRLRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRRRL, position_x=1440, position_y=350)
    RRLRRRR = BinaryTreeElement(RRLRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRLRRRR, position_x=1500, position_y=350)
    RRRRLLL = BinaryTreeElement(RRRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRLLL, position_x=1550, position_y=350)
    RRRRLLR = BinaryTreeElement(RRRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRLLR, position_x=1600, position_y=350)
    RRRRRLL = BinaryTreeElement(RRRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRLL, position_x=1650, position_y=350)
    RRRRRLR = BinaryTreeElement(RRRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRLR, position_x=1737, position_y=350)
    RRRRRRL = BinaryTreeElement(RRRRRR.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRRL, position_x=1785, position_y=350)
    RRRRRRR = BinaryTreeElement(RRRRRR.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRRR, position_x=1860, position_y=350)

    """ LEVEL 8 """

    RRRRRRLL = BinaryTreeElement(RRRRRRL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRRLL, position_x=1750, position_y=400)
    RRRRRRLR = BinaryTreeElement(RRRRRRL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRRLR, position_x=1820, position_y=400)
    RRRRRLLL = BinaryTreeElement(RRRRRLL.return_left_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRLLL, position_x=1600, position_y=400)
    RRRRRLLR = BinaryTreeElement(RRRRRLL.return_right_branch(), conclusion, main_premises, option_of_premises,
                                    option_of_conclusion, window)
    place_the_item_in_a_tree(RRRRRLLR, position_x=1700, position_y=400)

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
