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
                    premises["zarobki miesięczne"] = option_of_premises[index]
                elif 9 <= index <= 11:
                    premises["ostatni posiłek"] = option_of_premises[index]
                elif 12 <= index <= 14:
                    premises["ilość osób spożywających pizze"] = option_of_premises[index]
                elif 16 <= index <= 18:
                    premises["konkluzja(wybór pizzy):"] = option_of_conclusion[index - 16]
                    one_hundred_examples[number].update(premises)

    # for key, value in one_hundred_examples.items():
    #     print(f"{key} : {value}")

    window = Tk()
    window.geometry('1400x800+50+50')
    window.title("Drzewo decyzyjne")
    conclusion = "konkluzja(wybór pizzy):"
    main_premises = list(premises.keys())
    node = BinaryTreeElement(one_hundred_examples, conclusion, main_premises, option_of_premises, option_of_conclusion,
                             window)
    place_the_item_in_a_tree(node, position_x=650, position_y=0)
    left_leaf = BinaryTreeElement(node.return_left_branch(), conclusion, main_premises, option_of_premises,
                                  option_of_conclusion, window)
    place_the_item_in_a_tree(left_leaf, position_x=200, position_y=50)
    right_leaf = BinaryTreeElement(node.return_right_branch(), conclusion, main_premises, option_of_premises,
                                   option_of_conclusion, window)
    place_the_item_in_a_tree(right_leaf, position_x=860, position_y=50)
    left_left_leaf = BinaryTreeElement(left_leaf.return_left_branch(), conclusion, main_premises, option_of_premises,
                                       option_of_conclusion, window)
    place_the_item_in_a_tree(left_left_leaf, position_x=150, position_y=100)
    left_right_leaf = BinaryTreeElement(left_leaf.return_right_branch(), conclusion, main_premises, option_of_premises,
                                        option_of_conclusion, window)
    place_the_item_in_a_tree(left_right_leaf, position_x=300, position_y=100)
    right_right_leaf = BinaryTreeElement(right_leaf.return_right_branch(), conclusion, main_premises,
                                         option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_right_leaf, position_x=1120, position_y=100)
    right_left_leaf = BinaryTreeElement(right_leaf.return_left_branch(), conclusion, main_premises, option_of_premises,
                                        option_of_conclusion, window)
    place_the_item_in_a_tree(right_left_leaf, position_x=700, position_y=100)
    left_right_left_leaf = BinaryTreeElement(left_right_leaf.return_left_branch(), conclusion, main_premises,
                                             option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(left_right_left_leaf, position_x=250, position_y=150)
    left_right_right_leaf = BinaryTreeElement(left_right_leaf.return_right_branch(), conclusion, main_premises,
                                              option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(left_right_right_leaf, position_x=330, position_y=150)
    right_left_left_leaf = BinaryTreeElement(right_left_leaf.return_left_branch(), conclusion, main_premises,
                                             option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_left_left_leaf, position_x=650, position_y=150)
    right_left_right_leaf = BinaryTreeElement(right_left_leaf.return_right_branch(), conclusion, main_premises,
                                              option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_left_right_leaf, position_x=720, position_y=150)
    right_right_left_leaf = BinaryTreeElement(right_right_leaf.return_left_branch(), conclusion, main_premises,
                                              option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_right_left_leaf, position_x=970, position_y=150)
    right_right_right_leaf = BinaryTreeElement(right_right_leaf.return_right_branch(), conclusion, main_premises,
                                               option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_right_right_leaf, position_x=1170, position_y=150)
    left_right_right_left_leaf = BinaryTreeElement(left_right_right_leaf.return_left_branch(), conclusion,
                                                   main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(left_right_right_left_leaf, position_x=200, position_y=200)
    left_right_right_right_leaf = BinaryTreeElement(left_right_right_leaf.return_right_branch(), conclusion,
                                                    main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(left_right_right_right_leaf, position_x=450, position_y=200)
    right_left_right_left_leaf = BinaryTreeElement(right_left_right_leaf.return_left_branch(), conclusion,
                                                   main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_left_right_left_leaf, position_x=680, position_y=200)
    right_left_right_right_leaf = BinaryTreeElement(right_left_right_leaf.return_right_branch(), conclusion,
                                                    main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_left_right_right_leaf, position_x=730, position_y=200)
    right_right_left_left_leaf = BinaryTreeElement(right_right_left_leaf.return_left_branch(), conclusion,
                                                    main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_right_left_left_leaf, position_x=960, position_y=200)
    right_right_left_right_leaf = BinaryTreeElement(right_right_left_leaf.return_right_branch(), conclusion,
                                                    main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_right_left_right_leaf, position_x=1080, position_y=200)
    right_right_right_left_leaf = BinaryTreeElement(right_right_right_leaf.return_left_branch(), conclusion,
                                                    main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_right_right_left_leaf, position_x=1140, position_y=200)
    right_right_right_right_leaf = BinaryTreeElement(right_right_right_leaf.return_right_branch(), conclusion,
                                                     main_premises, option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(right_right_right_right_leaf, position_x=1200, position_y=200)
    window.mainloop()

    # test obsługi wyłapywania wyjątków:
    left_left_left_leaf = BinaryTreeElement(left_left_leaf.return_left_branch(), conclusion, main_premises,
                                            option_of_premises, option_of_conclusion, window)
    place_the_item_in_a_tree(left_left_left_leaf, position_x=800, position_y=500)


if __name__ == "__main__":
    run_example()
