from mainWindow import *

def main():
    root = tk.Tk()
    demo = App(root)

    root.mainloop()

if __name__ == '__main__':
    main()

'''
                 2

standart      expensive        cheap

  train          car       male      female

                            bus     0         1

                                   bus       train
'''