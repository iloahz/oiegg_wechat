WECHAT FOR OIEGG
================

FEATURE
-------
*   View top 10 topics on oiegg.com.
*   View information about full time jobs and intern.
*   View academic activities.

DEV LOG
-------
*   2013.02.12 first edition, support top 10, add pattern support.

DEPLOYMENT
----------
*   install `requirements.txt` and activate
*   set 'config.py'
*   run 'init.py'(**ONLY ONCE**)
*   run server

MAINTANCE
---------
*   `GET` */topten*
    *   `GET` */topten/update* updates top 10 topics
*   `GET` */pattern* shows an interactive interface
    `POST` */pattern* updates pattern(<input>, <output>)
    *   `GET` *pattern/<input>* returns the corresponding output
