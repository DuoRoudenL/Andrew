import hashlib

class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


    def __str__(self):
        return f"{self.username},{self.first_name},{self.last_name},{self.password}"

class Data:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError as e:
            print(e)
        
    def write(self, data_lines):
        try:
            with open(self.filename, 'a') as file:
                file.writelines(data_lines)
        except FileNotFoundError as e:
            print(e)

    def view(self):
        try:
            print(''.join(self.read()))
        except FileNotFoundError as e:
            print(e)
        
    def delete(self, target_data):
        try:
            data_lines = self.read()
            data_lines = [line for line in data_lines if target_data not in line]
            self.write(data_lines)
        except FileNotFoundError as e:
            print(e)
    
    def sort(self, key=None, reverse=False):
        try:
            data_lines = self.read()
            data_lines.sort(key=key, reverse=reverse)
            self.write(data_lines)
        except FileNotFoundError as e:
            print(e)

    def edit(self, oldest_data, new_data):
        try:
            data_lines = self.read()
            data_lines = [line.replace(oldest_data, new_data) for line in data_lines]
            self.write(data_lines)
        except FileNotFoundError as e:
            print(e)
    
    def search(self, query):
        try:
            data_lines = self.read()
            result = [line for line in data_lines if query in line]
            return ''.join(result)
        except FileNotFoundError as e:
            print(e)

def save_user(user, data_manager):
    data_manager.write(str(user) + '\n')

def register_user(data_manager):
    username = input("Введите логин: ")
    while not is_username_unique(username, data_manager):
        print("Этот логин уже занят. Пожалуйста, выберите другой.")
        username = input("Введите логин: ")
    password = input("Введите пароль: ")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    user = User(first_name, last_name, username, password)
    save_user(user, data_manager)
    print(f"Пользователь {user.first_name} {user.last_name} зарегистрирован с логином {user.username}")

def is_username_unique(username, data_manager):
    users = data_manager.read()
    for user in users:
        user_username, _, _, _ = user.split(',')
        if username == user_username:
            return False
    return True


def main():
    manager = Data('data.txt')
    register_user(manager)

if __name__ == "__main__":
    main()