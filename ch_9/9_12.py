""""""
import admin_privileges


def main():
    admin = admin_privileges.Admin('Ankka', 'Pukki', 22, 'Cyber security')
    admin.privileges.show_privileges()

if __name__ == "__main__":
    main()
