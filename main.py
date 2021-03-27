from var import * 
from auth import *
from c360api import *
from mcapi import *
import schedule
import time


def main():
    Oauth_Jwt()
    c360_segmentation()
    mc_ingest()


if __name__ == "__main__":
    main()
    """ schedule.every(1).minutes.do(main())
    while True:
        schedule.run_pending()
        time.sleep(1) """
