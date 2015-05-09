def removeBlankLines(fileName):
    with open(fileName, "r") as input:
        lines = [i for i in input if i[:-1]]
        with open(fileName, "w") as input:
            input.writelines(lines)
    return


