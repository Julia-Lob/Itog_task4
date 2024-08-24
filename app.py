#task_4
import pandas as pd

if __name__ == '__main__':
    # Загрузка данных из data.csv
    dataframe = pd.read_csv('data.csv')
    print (f"количество строк в файле данных:   {len(dataframe)}")
    # Вычисление средней зарплаты всех сотрудников
    average_salary = dataframe['salary'].mean()
    print(f"Средняя зарплата всех сотрудников: {average_salary}")

    # Отбор сотрудников старше 30 лет
    print("Сотрудники старше 30 лет:")
    print (dataframe.loc[(dataframe['age'] > 30)])

