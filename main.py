# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from multiprocessing import Process

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #모든 워크스페이스를 불러옴.
    #근데 어짜피 한디비에서 긁어올때 순서대로 가져오지 않나?

    workspace = ['a12bdcaed','c12bd3aed','d12dd32ed'];
    data = []
    #16진수인 워크스페이스 DB들을 10진수로 변환한 후 순서대로 나열한다.
    for i in workspace:
        data.append(int(i,16))

    print(sorted(data))

    p = Process(target=print_hi, args=('bob',))
    p.start()
    p.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
