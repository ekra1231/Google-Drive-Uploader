import mega

m = Mega.from_credentials("#email","#password")
                    filename=m.download_from_url(url)
                    print("Downloading Complete Mega :", filename) 