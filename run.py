from apiserver import create_apiserver


apiserver = create_apiserver("development")


if __name__ == "__main__":
    apiserver.run()
