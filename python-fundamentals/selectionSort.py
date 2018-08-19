#                         [ Selection Sort ]

# Objectives:
# ===============================================
# <> Shall take in a list with a bunch of numbers
# <> Shall sort the numbers executing Selection Sort
# ==================================================


def selectionSort( _list ):
    current_item = 0
    while (current_item < len(_list)):
        for next_item in range(len(_list)):
            if (_list[next_item] > _list[current_item]):
                _list[current_item], _list[next_item] = _list[next_item], _list[current_item]
        current_item += 1
    return _list

if __name__ == '__main__':
    print ("")
    print ("Array before 'Selection Sort' is applied to it: {}".format([4,2,5,0,3,1,6]))
    print ("Array after  'Selection Sort' has been applied: {}".format(selectionSort([4,2,5,0,3,1,6])))
    print ("")
