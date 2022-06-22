from src.delegators.app_delegator import AppDelegator

def main():
    AppDelegator() \
        .apply_config() \
        .read_files() \
        .convert_files()

if __name__ == '__main__':
    main()
