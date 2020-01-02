import loggerService
import reverseRemove
import systemd.daemon

if __name__ == '__main__':
    loggerService.log_init()
    reverseRemove.remove_dir()
