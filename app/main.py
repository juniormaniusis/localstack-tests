import pymysql
import os
import time

# Conecta ao banco de dados MySQL
def connect_to_mysql():
    time.sleep(10)  # Aguarda o MySQL iniciar
    connection = pymysql.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DATABASE', 'mydatabase'),
        port=3306
    )
    return connection


# Cria a tabela "dishes"
def create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dishes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                dish_name VARCHAR(255),
                date_cooked DATE,
                chef_name VARCHAR(100)
            )
        ''')
        connection.commit()
        print("Table 'dishes' created")


# Insere um prato no histórico
def insert_dish(connection, dish_name, date_cooked, chef_name):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO dishes (dish_name, date_cooked, chef_name) VALUES (%s, %s, %s)",
            (dish_name, date_cooked, chef_name)
        )
        connection.commit()
        print(f"Dish '{dish_name}' cooked by {chef_name} on {date_cooked} inserted")


# Realiza a operação de SELECT para listar os pratos
def select_dishes(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM dishes")
        result = cursor.fetchall()
        print("Historical Dishes:")
        for row in result:
            print(f"ID: {row[0]}, Dish: {row[1]}, Date: {row[2]}, Chef: {row[3]}")


if __name__ == "__main__":
    connection = connect_to_mysql()
    create_table(connection)
    
    # Exemplo de inserção de pratos no histórico
    insert_dish(connection, "Spaghetti Carbonara", "2023-09-24", "Chef Luigi")
    insert_dish(connection, "Beef Wellington", "2023-09-25", "Chef Gordon")
    insert_dish(connection, "Chicken Alfredo", "2023-09-26", "Chef Mario")
    
    # Exibir os pratos cozinhados
    select_dishes(connection)
    
    connection.close()