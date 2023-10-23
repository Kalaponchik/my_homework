from  data_create import input_user_data

def input_data ():
    name,surname,phone,adress= input_user_data()
    var= int(input(f'\n В каком формате записать данные?\n'
              f'1 Вариант:\n'
              f'{name}\n'
              f'{surname}\n'
              f'{phone}\n'
              f'{adress}\n\n'
              f'2 Вариант:\n'
              f'{name};{surname};{phone};{adress}n\n'
              f'\n Ваш выбор:'
              ))
    if var ==1:
         with open ("data_first_variant.csv","a", encoding= "utf-8") as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else: 
        with open ("data_first_variant.csv","a", encoding= "utf-8") as file:
            file.write (f'{name};{surname};{phone};{adress}n\n')


def print_data ():
    print ("1 файл")
    with open ("data_first_variant.csv","r", encoding= "utf-8") as file:
        data = file.readlines()
        for i in data:
            print (i, end="")


    print ("2 файл")
    with open ("data_second_variant.csv","r", encoding= "utf-8") as file:
        data = file.readlines()
        for i in data:
            if i !="\n":
             print (i, end="")
def delete_data ():
    lines=[]
    with open ("data_second_variant.csv","r", encoding= "utf-8") as file:
        data = file.radlines()
        count = 0
        for i in data:
            if i.strip():
                count +=1
                print (str(count) + '.'+ i,end="")
                lines.append(i)
            else:
                print (i, end="")
    var = int (input(f'\n Какую запись удалить?\n'
                     f'\n Ваш выбор:'))
    while var <1 or var > count:
        var= int (input ("Ошибка!Ваш выбор:"))
    with open ("data_second_variant.csv","w", encoding= "utf-8") as file:
        currentlineIndex=0
        for line in lines:
            currentlineIndex +=1
            if currentlineIndex !=var:
                file.write(line)
                file.write("\n")
                    

