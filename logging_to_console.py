import logging

# severity levels indicates wich message will log
# define it in basic config
# Debug logs all 
# info logs = and above info not debug
# warning logs = and above info not info or debug
# error logs = error and above info not warning, info or debug
# critical logs only critical not error,  warning, info or debug

# in basicConfig we define the file format of log


def main() -> None:
    logging .basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-d %H:%M:S",
        filename="basic.log",
    )

    logging.debug("This is a debug message")
    logging.info("This is an info  message")
    logging.warning("This is a warning  message")
    logging.error("This is an error  message")
    logging.critical("This is a critical message")

if __name__ == "__main__":
    main()