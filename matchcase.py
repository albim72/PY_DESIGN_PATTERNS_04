def provideAccess(user):
    return {
        "username":user,
        "password":"admin"
    }

def runMatch():
    user = input("podaj swoją nazwę użytkownika: ")

    match user:
        case "Olga":
            print("Olga nie ma dostępu do bazy danych SYSDB...., tyko do api code")
        case "Adam":
            print("Adam nie ma dostępu do bazy danych SYSDB...., tyko do fronted code")
        case "Olaf":
            print("Olaf ma dostęp do bazy danych SYSDB!!!")
            print(provideAccess("Olaf"))
        case _:
            print("taki user nie istnieje!")


if __name__ == '__main__':
    for _ in range(3):
        runMatch()

