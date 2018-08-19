#                         [ Insertion Sort ]

# Objectives:
# ===============================================
# <> Shall take in a list with a bunch of numbers
# <> Shall sort the numbers executing Insertion Sort
# ==================================================


def selectionSort( _list ):
    current_item = 1
    while (current_item < len(_list)):
        for item in range(0, current_item):
            if (_list[item] > _list[current_item]):
                _list[current_item], _list[item] = _list[item], _list[current_item]
        current_item += 1
    return _list


if __name__ == '__main__':
    print ("")
    print ("Array before 'Insertion Sort' is applied to it: {}".format([4,2,5,0,3,1,6]))
    print ("Array after  'Insertion Sort' has been applied: {}".format(selectionSort([4,2,5,0,3,1,6])))
    print ("")


