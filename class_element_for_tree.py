import _tkinter
from tkinter import *
from math import log2


class BinaryTreeElement:
    def __init__(self, dict_elements: dict[int, dict[str, str]], conclusion: str, main_premises: list[str],
                 premises_option: list[str], conclusion_option: list[str], window) -> None:
        self.dict_elements = dict_elements
        self.conclusion = conclusion
        self.main_premises = main_premises
        self.premises_option = premises_option
        self.conclusion_option = conclusion_option
        self.window = window

    def return_conclusion_tab(self) -> list[int]:
        conclusion_tab = [0 for _ in range(len(self.conclusion_option))]
        try:
            for key, value in self.dict_elements.items():
                if value[self.conclusion] == self.conclusion_option[0]:
                    conclusion_tab[0] += 1
                elif value[self.conclusion] == self.conclusion_option[1]:
                    conclusion_tab[1] += 1
                else:
                    conclusion_tab[2] += 1
            return conclusion_tab
        except AttributeError:
            return ""

    def calculate_conclusion_entropy(self) -> float:
        conclusion_entropy = 0.0
        for number in self.return_conclusion_tab():
            if number == 0:
                conclusion_entropy += 0
            else:
                conclusion_entropy += -(number / len(self.dict_elements)) * log2(number / len(self.dict_elements))
        return conclusion_entropy

    def calculate_entropy_for_premise_return_info(self, main_premise: str, premise: str) -> float:
        positive_premise_entropy = 0.0
        negative_premise_entropy = 0.0

        positive_data_to_entropy = [0 for _ in range(len(self.return_conclusion_tab()))]
        negative_data_to_entropy = [0 for _ in range(len(self.return_conclusion_tab()))]
        try:
            for key, value in self.dict_elements.items():
                if value[main_premise] == premise and value[self.conclusion] == self.conclusion_option[0]:
                    positive_data_to_entropy[0] += 1
                elif value[main_premise] == premise and value[self.conclusion] == self.conclusion_option[1]:
                    positive_data_to_entropy[1] += 1
                elif value[main_premise] == premise and value[self.conclusion] == self.conclusion_option[2]:
                    positive_data_to_entropy[2] += 1
            # print(positive_data_to_entropy)
            for number in range(len(self.return_conclusion_tab())):
                negative_data_to_entropy[number] = self.return_conclusion_tab()[number] - positive_data_to_entropy[number]
            # print(negative_data_to_entropy)
            for index, number in enumerate(positive_data_to_entropy):
                if number == 0:
                    positive_premise_entropy += 0
                else:
                    positive_premise_entropy += -(number / sum(positive_data_to_entropy)) * \
                                            log2(number / sum(positive_data_to_entropy))
            for index, number in enumerate(negative_data_to_entropy):
                if number == 0:
                    negative_premise_entropy += 0
                else:
                    negative_premise_entropy += -(number / sum(negative_data_to_entropy)) * \
                                            log2(number / sum(negative_data_to_entropy))
            # print(f"I+({premise}) = {positive_premise_entropy}")
            # print(f"I-({premise}) = {negative_premise_entropy}")
            return positive_premise_entropy * (sum(positive_data_to_entropy) / len(self.dict_elements)) + \
               negative_premise_entropy * (sum(negative_data_to_entropy) / len(self.dict_elements))
        except AttributeError:
            return ""

    def return_entropy_tab(self) -> list[float]:
        entropy = []
        if len(self.main_premises) >= 1:
            for option in self.premises_option[:4]:
                value = self.calculate_entropy_for_premise_return_info(main_premise=self.main_premises[0],
                                                                       premise=option)
                entropy.append(value)
        if len(self.main_premises) >= 2:
            for option in self.premises_option[4:6]:
                value = self.calculate_entropy_for_premise_return_info(main_premise=self.main_premises[1],
                                                                       premise=option)
                entropy.append(value)
        if len(self.main_premises) >= 3:
            for option in self.premises_option[6:9]:
                value = self.calculate_entropy_for_premise_return_info(main_premise=self.main_premises[2],
                                                                       premise=option)
                entropy.append(value)
        if len(self.main_premises) >= 4:
            for option in self.premises_option[9:12]:
                value = self.calculate_entropy_for_premise_return_info(main_premise=self.main_premises[3],
                                                                       premise=option)
                entropy.append(value)
        if len(self.main_premises) >= 5:
            for option in self.premises_option[12:]:
                value = self.calculate_entropy_for_premise_return_info(main_premise=self.main_premises[4],
                                                                       premise=option)
                entropy.append(value)
        return entropy

    def return_information_gain(self) -> list[float]:
        information_gain = []
        try:
            for value in self.return_entropy_tab():
                result = self.calculate_conclusion_entropy() - value
                information_gain.append(result)
            return information_gain
        except TypeError:
            return ""

    def find_best_entropy(self) -> str:
        if self.calculate_conclusion_entropy() != 0:
            number = 0
            best_entropy = self.return_information_gain()[number]
            for index, value in enumerate(self.return_information_gain()):
                if value > best_entropy:
                    best_entropy = value
                    number = index
                else:
                    continue
            return self.premises_option[number]
        else:
            for index, value in enumerate(self.return_conclusion_tab()):
                if value > 0:
                    return self.conclusion_option[index]

    def return_best_main_premise(self) -> str:
        if self.calculate_conclusion_entropy() != 0:
            best_entropy = self.find_best_entropy()
            for index, premise in enumerate(self.premises_option):
                if premise == best_entropy:
                    if 0 <= index <= 3:
                        return self.main_premises[0]
                    if 4 <= index <= 5:
                        return self.main_premises[1]
                    if 6 <= index <= 8:
                        return self.main_premises[2]
                    if 9 <= index <= 11:
                        return self.main_premises[3]
                    if 12 <= index <= 14:
                        return self.main_premises[4]
        else:
            return ""

    def return_left_branch(self) -> dict[int, dict[str, str]]:
        left_branch = {}
        try:
            for key in self.dict_elements.keys():
                if self.dict_elements[key][self.return_best_main_premise()] == self.find_best_entropy():
                    left_branch[key] = self.dict_elements[key]
            return left_branch
        except:
            print("Brak kolejnych węzłów dla tej gałęzi")

    def return_right_branch(self) -> dict[int, dict[str, str]]:
        right_branch = {}
        try:
            for key in self.dict_elements.keys():
                if self.dict_elements[key][self.return_best_main_premise()] != self.find_best_entropy():
                    right_branch[key] = self.dict_elements[key]
            return right_branch
        except:
            print("Brak kolejnych węzłów dla tej gałęzi")

    def draw_element_on_tree(self, position_x: int, position_y: int) -> None:
        try:
            position_no = len(str(self.return_best_main_premise())) + len(str(self.find_best_entropy()))
            position_no = position_x + position_no * 4
            position_yes = len(str(self.return_best_main_premise())) + len(str(self.find_best_entropy()))
            position_yes = position_x - position_yes
            label_no = Label(self.window, text="NIE", font=("Times New Roman", 8))
            label_yes = Label(self.window, text="TAK", font=("Times New Roman", 8))
            label_node = Label(self.window, text=f"{self.return_best_main_premise()} {self.find_best_entropy()}",
                           justify="center", font=("Times New Roman", 10))
            label_node.place(x=position_x, y=position_y)
            if len(self.return_best_main_premise()) > 0:
                label_no.place(x=position_no, y=position_y + 30)
                label_yes.place(x=position_yes, y=position_y + 30)
        except _tkinter.TclError:
            return ""

    def __str__(self) -> str:
        if self.find_best_entropy() != self.conclusion_option[0] and \
                self.find_best_entropy() != self.conclusion_option[1] and \
                self.find_best_entropy() != self.conclusion_option[2] and self.calculate_conclusion_entropy() != 0.0:
            show_info_gain = ""
            print(f"I (konkluzja) -- {self.calculate_conclusion_entropy()}")
            print("j\t\t\tI-Ej")
            print(35 * '-')
            for index, unit_information_gain in enumerate(self.return_information_gain()):
                if unit_information_gain > 0:
                    show_info_gain += f"{index}\t\t\t{unit_information_gain}\n"
            return show_info_gain
        else:
            return ""
