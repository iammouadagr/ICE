import sys
import Ice

Ice.loadSlice('Server.ice')
import Server


def run(communicator):
    twoway = Server.HelloPrx.checkedCast(
        communicator.propertyToProxy('Hello.Proxy').ice_twoway().ice_secure(False))
    if not twoway:
        print("invalid proxy")
        sys.exit(1)

    oneway = Server.HelloPrx.uncheckedCast(twoway.ice_oneway())

    secure = False
    timeout = -1
    delay = 0

    menu()
    c = None
    while c != 'x':
        try:
            sys.stdout.write("==> ")
            sys.stdout.flush()
            c = sys.stdin.readline().strip()
            if c == 't':
                twoway.sayHello()
            elif c == 'k':
                twoway.shutdown()
            elif c == 'ft':
                res =twoway.findAllByTitle("Stronger")
                if res :
                    for song in res:
                        print(song)
                else:
                    print("No song found. ")
            elif c == 'fa':
                res = twoway.findAllByArtist("Kanye West")
                if res:
                    for song in res:
                        print(song)
                else:
                    print("No song found. ")
            elif c == 's':
                res = twoway.stream('62603660502487c54f562a11')
                print(res)
            elif c == 'x':
                pass  # Nothing to do
            else:
                print("unknown command `" + c + "\'")
                menu()

        except Ice.Exception as ex:
            print(ex)
def menu():
    print("""
    usage:
    t: send greeting as twoway
    k: shutdown server
    a: add Song
    ft: find by title
    fa: find by artist
    s: stream
    x: exit
     """)
    
with Ice.initialize(sys.argv, "config.client") as communicator:

    #
    # The communicator initialization removes all Ice-related arguments from argv
    #
    if len(sys.argv) > 1:
        print(sys.argv[0] + ": too many arguments")
        sys.exit(1)

    run(communicator)