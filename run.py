if __name__ == "__main__":
        try:
                __import__("Share").menu()
        except Exception as e:
                exit(str(e))
