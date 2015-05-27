#!/usr/bin/python
"""
Implments the class based merge sort algorithm
"""


class MergeSort(object):

    def divide_conquer(self, full_list):
        list_length = len(full_list)

        #   list with one item
        if list_length <= 1:
            return full_list
        else:
            mid = list_length / 2

            #   divide list into two halfs
            left_half = full_list[0:mid]
            right_half = full_list[mid:]

            #   conquer
            conquered_list_one = MergeSort().divide_conquer(left_half)
            conquered_list_two = MergeSort().divide_conquer(right_half)

        return MergeSort().merge(conquered_list_one, conquered_list_two)

    def merge(self, list_one, list_two):
        i, j, sorted_list = 0, 0, []
        length_one = len(list_one)
        length_two = len(list_two)

        #   while any of the list is not empty
        while(i < length_one) or (i < length_two):
            if(i < length_one) and (j < length_two):
                #   both lists have data
                if list_one[i] <= list_two[j]:
                    sorted_list.append(list_one[i])
                    i += 1
                else:
                    sorted_list.append(list_two[j])
                    j += 1
            elif i < length_one:
                #   only list one has data
                sorted_list.append(list_one[i])
                i += 1
            else:
                #   only list two has data
                sorted_list.append(list_two[j])
                j += 1
        else:
            return sorted_list









