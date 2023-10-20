from . import pymake


def main():
    cli = pymake.PyMakeCLI()
    cli.get_args()
    if cli.command == "create":
        cli.create_config()
    elif cli.command == "build":
        cli.build()
    else:
        print("Command not found")
        exit(4)

    
if __name__ == "__main__":
    main()