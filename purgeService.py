import loggerService
import reverseRemove
import settings

if __name__ == '__main__':
    loggerService.log_init()
    settings.createSettingsFile()
    reverseRemove.remove_dir()
