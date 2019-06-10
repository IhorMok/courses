# import sys
# import io
# print(dir(io))
# print(sys.stdin, sys.stdout, sys.stderr, sep= "\n")


# hendler = open("text.json").read()
# print(hendler)

# hendler = open("text.json", mode="rb")
# print(dir(hendler))
# print(hendler.raw)
# for line in hendler.readline():
#     print(hendler.tell())
#     print(line)
#
# hendler.close()




# n = 0
# print()
#
# try:
#     print(2/n)
# except Exception as err:
#     print(f"error type {err}", err )
# except:
# else:
#     print("done!!!")
# finally:
#     print("final print")

# for err in Exception.__subclasses__():
#     print(err)


with open("text.json") as json:
    print(json.readlines())


try:
    json = open("text.json")
    print(json.readlines())
finally:
    json.close()


class Contex:
    def __enter__(self):
        return open("text.json")

    def __exit__(self, typeErr, err, traceback):
        pass

with Contex as c:
    pass
print(c)








