import webview

tweet_url = "https://twitter.com/ibm_in/status/1725370954774175881"

webview.create_window("Embedded Tweet", tweet_url)
webview.start()
