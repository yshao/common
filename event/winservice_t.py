from winservice import Service, instart


class IService(Service):
    def start(self):
        self.runflag=True
        while self.runflag:
            self.sleep(10)
            self.log("I'm alive ...")
    def stop(self):
        self.runflag=False
        self.log("I'm done")

def main():
    instart(IService, 'aTest', 'Python Service Test')

if __name__ == '__main__':
    main()